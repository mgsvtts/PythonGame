import random
from Infrastructure.config_loader import (
    load_config,
    load_items,
    load_state,
    save_character_state,
)
from Infrastructure.printer import (
    print_character_dead,
    print_damage_taken,
    print_enemy_attack_result,
    print_enemy_dead,
    print_enemy_found,
)


def calculate_armor(actual=True):
    if actual:
        state = load_state()
    else:
        state = load_config()

    equipment = load_items(state["character"]["items"])

    armor_dict = {}
    for item in equipment:
        name = item["name"]
        if name not in armor_dict:
            armor_dict[name] = item["hp"]

    return sum(armor_dict.values())


def calculate_damage(actual=True):
    if actual:
        state = load_state()
    else:
        state = load_config()

    equipment = load_items(state["character"]["items"])
    damage = 0
    for item in equipment:
        if item["damage"] > damage:
            damage = item["damage"]

    return damage


def find_random_enemy():
    enemies = load_config()["enemy"]

    enemy = random.choice(enemies)

    print_enemy_found(enemy)

    return enemy


def try_kill_enemy(enemy, character):
    damage = character["damage"] + calculate_damage()
    enemy["hp"] -= damage

    print_enemy_attack_result(enemy, damage)

    if enemy["hp"] > 0:
        return False

    print_enemy_dead(character, enemy)

    character["money"] += enemy["money"]
    if enemy["items"]:
        character["items"] += enemy["items"]

    return True


def take_armor_damage(enemy, character):
    if character["armor"] >= enemy["damage"]:
        character["armor"] -= enemy["damage"]
    else:
        character["hp"] -= enemy["damage"] - character["armor"]
        character["armor"] = 0


def try_die(enemy, character):
    if character["armor"] > 0:
        take_armor_damage(enemy, character)
    else:
        character["hp"] -= enemy["damage"]

    print_damage_taken(character, enemy)

    if character["hp"] > 0:
        return False

    return True


def distinct_equipment(character):
    equipments = []
    for item in character["items"]:
        if item not in equipments:
            equipments.append(item)

    character["items"] = equipments


def handle_attack():
    enemy = find_random_enemy()
    character = load_state()["character"]

    somebody_died = False
    while somebody_died == False:
        dice = random.randint(1, 6)
        if dice > 3:
            somebody_died = try_kill_enemy(enemy, character)
        else:
            somebody_died = try_die(enemy, character)

    if character["hp"] <= 0:
        print_character_dead()
        raise Exception()

    distinct_equipment(character)
    save_character_state(character)

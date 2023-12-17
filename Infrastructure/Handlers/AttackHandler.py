import random
from Infrastructure.ConfigLoader import (
    LoadConfig,
    LoadItems,
    LoadState,
    SaveCharacterState,
)
from Infrastructure.Printer import (
    PrintCharacterDead,
    PrintDamageTaken,
    PrintEnemyAttackResult,
    PrintEnemyDead,
    PrintEnemyFound,
)


def CalculateArmor(actual=True):
    if actual:
        state = LoadState()
    else:
        state = LoadConfig()

    equipment = LoadItems(state["character"]["items"])

    armorDict = {}
    for item in equipment:
        name = item["name"]
        if name not in armorDict:
            armorDict[name] = item["hp"]

    return sum(armorDict.values())


def CalculateDamage(actual=True):
    if actual:
        state = LoadState()
    else:
        state = LoadConfig()

    equipment = LoadItems(state["character"]["items"])
    damage = 0
    for item in equipment:
        if item["damage"] > damage:
            damage = item["damage"]

    return damage


def FindRandomEnemy():
    enemies = LoadConfig()["enemy"]

    enemy = random.choice(enemies)

    PrintEnemyFound(enemy)

    return enemy


def TryKillEnemy(enemy, character):
    damage = character["damage"] + CalculateDamage()
    enemy["hp"] -= damage

    PrintEnemyAttackResult(enemy, damage)

    if enemy["hp"] > 0:
        return False

    PrintEnemyDead(character, enemy)

    character["money"] += enemy["money"]
    if enemy["items"]:
        character["items"] += enemy["items"]

    return True


def TakeArmorDamage(enemy, character):
    if character["armor"] >= enemy["damage"]:
        character["armor"] -= enemy["damage"]
    else:
        character["hp"] -= enemy["damage"] - character["armor"]
        character["armor"] = 0


def TryDie(enemy, character):
    if character["armor"] > 0:
        TakeArmorDamage(enemy, character)
    else:
        character["hp"] -= enemy["damage"]

    PrintDamageTaken(character, enemy)

    if character["hp"] > 0:
        return False

    return True


def DistinctEquipment(character):
    equipments = []
    for item in character["items"]:
        if item not in equipments:
            equipments.append(item)

    character["items"] = equipments


def HandleAttack():
    enemy = FindRandomEnemy()
    character = LoadState()["character"]

    somebodyDied = False
    while somebodyDied == False:
        dice = random.randint(1, 6)
        if dice > 3:
            somebodyDied = TryKillEnemy(enemy, character)
        else:
            somebodyDied = TryDie(enemy, character)

    if character["hp"] <= 0:
        PrintCharacterDead()
        raise Exception()

    DistinctEquipment(character)
    SaveCharacterState(character)

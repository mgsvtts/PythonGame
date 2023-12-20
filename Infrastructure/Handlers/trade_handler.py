from Infrastructure.config_loader import (
    load_items,
    load_state,
    save_character_state,
    save_character_state,
    save_mechant_state,
)
from Infrastructure.Handlers.attack_handler import calculate_armor
from Infrastructure.printer import (
    print_already_has_item,
    print_buy_completed,
    print_character_not_enough_money,
    print_items_to_sell,
    print_merchant_found,
    print_merchant_items,
    print_merchant_not_enough_money,
    print_sell_completed,
    print_healed,
    print_repaired
)


def check_already_has_item(character, item):
    if item["name"] in character["items"]:
        return True

    return False


def remove_merchant_item(merchant, character, item):
    result = []
    for merchant_item in merchant["items"]:
        if merchant_item != item["name"]:
            result.append(merchant_item)

    merchant["items"] = result
    character["armor"] += item["hp"]


def remove_character_item(character, item):
    result = []
    for character_item in character["items"]:
        if character_item != item["name"]:
            result.append(character_item)

    result = load_items(result)
    character["items"] = [item["name"] for item in result]
    character["armor"] = sum([item["hp"] for item in result])


def handle_buy(character, merchant):
    item = print_merchant_items()
    if item == "уйти":
        return

    loadedItem = load_items(item)[0]
    if character["money"] < loadedItem["cost"]:
        print_character_not_enough_money()
        return
    elif check_already_has_item(character, loadedItem):
        print_already_has_item()
        return

    character["money"] -= loadedItem["cost"]
    character["items"].append(loadedItem["name"])
    remove_merchant_item(merchant, character, loadedItem)

    print_buy_completed(loadedItem["name"])

    save_character_state(character)
    save_mechant_state(merchant)


def handle_sell(character, merchant):
    item = print_items_to_sell()
    if item == "уйти":
        return

    loaded_item = load_items(item)[0]
    if loaded_item["cost"] > merchant["money"]:
        print_merchant_not_enough_money(character)
        return

    character["money"] += loaded_item["cost"]
    merchant["items"].append(loaded_item["name"])
    merchant["money"] -= loaded_item["cost"]
    remove_character_item(character, loaded_item)

    print_sell_completed(character["name"])

    save_character_state(character)
    save_mechant_state(merchant)


def handle_heal(character, merchant):
    can_heal = int(character["money"] / 5)
    needed_heal = character["maxHp"] - character["hp"]

    if needed_heal > can_heal:
        needed_heal = can_heal

    character["hp"] += needed_heal
    character["money"] -= needed_heal * 5
    merchant["money"] += needed_heal * 5

    print_healed(needed_heal)
    save_character_state(character)
    save_mechant_state(merchant)


def handle_repair(character, merchant):
    can_repair = int(character["money"] / 2)
    needen_armor = calculate_armor() - character["armor"]

    if needen_armor > can_repair:
        needen_armor = can_repair

    character["armor"] += needen_armor
    character["money"] -= needen_armor * 2
    merchant["money"] += needen_armor * 2

    print_repaired(needen_armor)
    save_character_state(character)
    save_mechant_state(merchant)


def handle_trade():
    state = load_state()
    character = state["character"]
    merchant = state["seller"]

    choice = 0
    while choice != 5:
        choice = print_merchant_found()
        if choice == 1:
            handle_buy(character, merchant)
        elif choice == 2:
            handle_sell(character, merchant)
        elif choice == 3:
            handle_heal(character, merchant)
        elif choice == 4:
            handle_repair(character, merchant)
        elif choice == 5:
            print("Пока-пока")

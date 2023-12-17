from Infrastructure.ConfigLoader import (
    LoadItems,
    LoadState,
    SaveCharacterState,
    SaveMerchantState,
)
from Infrastructure.Handlers.AttackHandler import CalculateArmor
from Infrastructure.Printer import (
    PrintAlreadyHasItem,
    PrintBuyCompleted,
    PrintCharacterNotEnoughMoney,
    PrintItemsToSell,
    PrintMerchantFound,
    PrintMerchantItems,
    PrintMerchantNotEnoughMoney,
    PrintSellCompleted,
)


def CheckAlreadyHasItem(character, item):
    if item["name"] in character["items"]:
        return True

    return False


def RemoveMerchantItem(merchant, character, item):
    result = []
    for merchantItem in merchant["items"]:
        if merchantItem != item["name"]:
            result.append(merchantItem)

    merchant["items"] = result
    character["armor"] += item["hp"]


def RemoveCharacterItem(character, item):
    result = []
    for characterItem in character["items"]:
        if characterItem != item["name"]:
            result.append(characterItem)

    result = LoadItems(result)
    character["items"] = [item["name"] for item in result]
    character["armor"] = sum([item["hp"] for item in result])


def HandleBuy(character, merchant):
    item = PrintMerchantItems()
    if item == "уйти":
        return

    loadedItem = LoadItems(item)[0]
    if character["money"] < loadedItem["cost"]:
        PrintCharacterNotEnoughMoney()
        return
    elif CheckAlreadyHasItem(character, loadedItem):
        PrintAlreadyHasItem()
        return

    character["money"] -= loadedItem["cost"]
    character["items"].append(loadedItem["name"])
    RemoveMerchantItem(merchant, character, loadedItem)

    PrintBuyCompleted(loadedItem["name"])

    SaveCharacterState(character)
    SaveMerchantState(merchant)


def HandleSell(character, merchant):
    item = PrintItemsToSell()
    if item == "уйти":
        return

    loadedItem = LoadItems(item)[0]
    if loadedItem["cost"] > merchant["money"]:
        PrintMerchantNotEnoughMoney(character)
        return

    character["money"] += loadedItem["cost"]
    merchant["items"].append(loadedItem["name"])
    merchant["money"] -= loadedItem["cost"]
    RemoveCharacterItem(character, loadedItem)

    PrintSellCompleted(character["name"])

    SaveCharacterState(character)
    SaveMerchantState(merchant)


def HandleHeal(character, merchant):
    canHeal = int(character["money"] / 5)
    neededHeal = character["maxHp"] - character["hp"]

    if neededHeal > canHeal:
        neededHeal = canHeal

    character["hp"] += neededHeal
    character["money"] -= neededHeal * 5
    merchant["money"] += neededHeal * 5

    SaveCharacterState(character)
    SaveMerchantState(merchant)


def HandleRepair(character, merchant):
    canRepair = int(character["money"] / 2)
    neededArmor = CalculateArmor() - character["armor"]

    if neededArmor > canRepair:
        neededArmor = canRepair

    character["armor"] += neededArmor
    character["money"] -= neededArmor * 2
    merchant["money"] += neededArmor * 2

    SaveCharacterState(character)
    SaveMerchantState(merchant)


def HandleTrade():
    state = LoadState()
    character = state["character"]
    merchant = state["seller"]

    choice = 0
    while choice != 3:
        choice = PrintMerchantFound()
        if choice == 1:
            HandleBuy(character, merchant)
        elif choice == 2:
            HandleSell(character, merchant)
        elif choice == 3:
            HandleHeal(character, merchant)
        elif choice == 4:
            HandleRepair(character, merchant)
        elif choice == 5:
            print("Пока-пока")

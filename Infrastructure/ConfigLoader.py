import json
import Infrastructure


def LoadConfig():
    file = open("game.json", encoding="UTF8")
    return json.load(file)


def LoadItems(items):
    lowerItems = [item.lower() for item in items]
    loadedItems = LoadConfig()["items"]
    result = []
    for item in loadedItems:
        if item["name"].lower() in lowerItems or item["name"].lower() == items:
            result.append(item)

    return result


def LoadState():
    file = open("state.json", encoding="UTF8")
    return json.load(file)


def InitState():
    state = LoadConfig()
    armor = Infrastructure.Handlers.AttackHandler.CalculateArmor(False)
    state["character"].update({"maxHp": state["character"]["hp"]})
    state["character"].update({"armor": armor})
    initState = {"character": state["character"], "seller": state["seller"]}

    jsonState = json.dumps(initState)

    gameState = open("state.json", "w", encoding="UTF8")

    gameState.write(jsonState)

    gameState.close()


def GetCurrentState():
    file = open("state.json", encoding="UTF8")
    state = json.load(file)
    file.close()

    return state


def SaveState(state):
    file = open("state.json", "w", encoding="UTF8")
    file.write(json.dumps(state))
    file.close()


def SaveCharacterState(character):
    state = GetCurrentState()

    state["character"] = character

    SaveState(state)


def SaveMerchantState(merchant):
    state = GetCurrentState()

    state["seller"] = merchant

    SaveState(state)

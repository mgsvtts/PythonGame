import json
import Infrastructure


def load_config():
    file = open("game.json", encoding="UTF8")
    return json.load(file)


def load_items(items):
    lower_items = [item.lower() for item in items]
    loaded_items = load_config()["items"]
    result = []
    for item in loaded_items:
        if item["name"].lower() in lower_items or item["name"].lower() == items:
            result.append(item)

    return result


def load_state():
    file = open("state.json", encoding="UTF8")
    return json.load(file)


def init_state():
    state = load_config()
    armor = Infrastructure.Handlers.attack_handler.calculate_armor(False)
    state["character"].update({"maxHp": state["character"]["hp"]})
    state["character"].update({"armor": armor})
    init_state = {"character": state["character"], "seller": state["seller"]}

    json_state = json.dumps(init_state)

    game_state = open("state.json", "w", encoding="UTF8")

    game_state.write(json_state)

    game_state.close()


def get_current_state():
    file = open("state.json", encoding="UTF8")
    state = json.load(file)
    file.close()

    return state


def save_state(state):
    file = open("state.json", "w", encoding="UTF8")
    file.write(json.dumps(state))
    file.close()


def save_character_state(character):
    state = get_current_state()

    state["character"] = character

    save_state(state)


def save_character_state(merchant):
    state = get_current_state()

    state["seller"] = merchant

    save_state(state)

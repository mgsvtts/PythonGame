import os
from Infrastructure.Handlers.action_handler import handle_action
from Infrastructure.printer import print_menu


def play():
    try:
        while True:
            handle_action(print_menu())
    except:
        if os.path.exists("state.json"):
            os.remove("state.json")

        print("Игра окончена")

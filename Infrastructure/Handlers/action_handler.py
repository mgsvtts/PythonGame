from Infrastructure.Handlers.attack_handler import handle_attack
from Infrastructure.Handlers.trade_handler import handle_trade
from Infrastructure.printer import print_stats


def handle_action(action):
    if action == 1:
        handle_attack()
    elif action == 2:
        handle_trade()
    elif action == 3:
        print_stats()
    elif action == 4:
        raise Exception("Конец игры")
    else:
        print("Герой так не умеет")

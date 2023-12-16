from Infrastructure.Handlers.AttackHandler import HandleAttack
from Infrastructure.Handlers.TradeHandler import HandleTrade
from Infrastructure.Printer import PrintStats

def HandleAction(action):
    if(action == 1):
        HandleAttack()
    elif(action==2):
        HandleTrade()
    elif(action==3):
        PrintStats()
    else:
        print("Герой так не умеет")

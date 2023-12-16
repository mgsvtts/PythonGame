from Infrastructure.Handlers.ActionHandler import HandleAction
from Infrastructure.Printer import PrintMenu

def Play():
    try:
        while(True):
            HandleAction(PrintMenu())
    except:
        print("Игра окончена")
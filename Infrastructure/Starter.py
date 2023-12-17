import os
from Infrastructure.Handlers.ActionHandler import HandleAction
from Infrastructure.Printer import PrintMenu

def Play():
    try:
        while(True):
            HandleAction(PrintMenu())
    except:
        if os.path.exists("state.json"):
            os.remove("state.json")
       
        print("Игра окончена")
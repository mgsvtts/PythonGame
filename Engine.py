import json
from Infrastructure.ConfigLoader import LoadConfig
from Infrastructure.Starter import Play

def Init():
    state = LoadConfig()
    initState  = {"character":state["character"], 
                  "seller":state["seller"]}
    
    jsonState = json.dumps(initState)

    gameState = open("state.json", "w", encoding='UTF8')

    gameState.write(jsonState)

    gameState.close()

Init()

Play()

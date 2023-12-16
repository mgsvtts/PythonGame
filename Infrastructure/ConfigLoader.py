import json

def LoadConfig():
    file = open('game.json', encoding='UTF8')
    return json.load(file)

def LoadItems(items):
    loadedItems = LoadConfig()["items"]
    result = []
    for item in loadedItems:
        if(item["name"] in items):
            result.append(item)
            
    return result
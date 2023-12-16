from Infrastructure.ConfigLoader import LoadConfig


def PrintMenu():
    print("1 - ринуться в атаку")
    print("2 - найти ближайшего торговца")
    print("3 - посмотреть на себя красивого")
    print("Выбери действие: ")
    return int(input())

def PrintStats():
    character = LoadConfig()["character"]
    print(character["hp"])

def PrintEnemyFound(enemy):
    print(f"На пути вам попался {enemy["name"]}")
    
def PrintDiceResult(dice):
    print(f"Вам выпало {dice}")
    
def PrintEnemyAttackResult(enemy, damage):
    if(enemy["hp"]<=0):
        hp = 0
    else:
        hp = enemy["hp"]
    
    print(f"Вы нанесли {damage} урона")
    print(f"У {enemy["name"]} осталось {hp} здоровья")
   
def PrintEnemyDead(enemy):
    message = f"{enemy["name"]} не сдержал вашего настиска и помер, "
    
    if(enemy["items"]):
        message += "оставив после себя "
        for item in enemy["items"]:
            message += item + ", "
    else:
        message = "ничего не оставив после себя"
    
    if(message[-2] == ','):
        message = message[:-2]
    
    print(message)
   
def PrintDamageTaken(character, enemy):
    if(character["hp"] <=0):
        hp = 0
    else:
        hp = character["hp"]
     
    print(f"{enemy["name"]} атаковал вас на {enemy["damage"]} урона, оставив вам {hp} здоровья")
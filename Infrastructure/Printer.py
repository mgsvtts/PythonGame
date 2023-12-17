from Infrastructure.ConfigLoader import LoadItems, LoadState
import Infrastructure

def PrintMenu():
    print("1 - ринуться в атаку")
    print("2 - найти ближайшего торговца")
    print("3 - посмотреть на себя красивого")
    print("4 - закончить игру")
    print("Выбери действие: ")
    return int(input())

def PrintItems(items):
    for item in items:
        print(f"- {item["name"]}")
        print(f"    цена {item["cost"]}")
        print(f"    урон {item["damage"]}")
        print(f"    защита {item["hp"]}")

def PrintStats():
    character = LoadState()["character"]
    equipments = LoadItems(character["items"])
    damage = character["damage"] + Infrastructure.Handlers.AttackHandler.CalculateDamage()

    print("=" * 30)
    print(f"Ваше имя: {character["name"]} и вы великий воин")
    print(f"Броня: {character["armor"]}")
    print(f"Здоровье {character["hp"]} из {character["maxHp"]}")
    print(f"Врожденный урон {character["damage"]}")
    print(f"Урон с надетым снаряжением {damage}")
    print(f"Червонцы {character["money"]}")
    print("Инвентарь:")
    PrintItems(equipments)
    print("=" * 30)

def PrintAlreadyHasItem():
    print("У вас уже есть этот предмет")

def PrintCharacterNotEnoughMoney():
    print("К сожалению, у тебя не хватает денег")

def PrintMerchantNotEnoughMoney(character):
    print(f"Извини, {character["name"]}, но твой предмет слишком дорогой для меня")

def PrintSellCompleted(character):
    print(f"Конечно, {character}, я с радостью куплю у тебя это")

def PrintMerchantFound():
    merchant = LoadState()["seller"]
    print(f"Привет, я {merchant["name"]}, что бы вы хотели?")
    print("1 - купить")
    print("2 - продать")
    print("3 - уйти")
    return int(input())

def PrintMerchantItems():
    merchant = LoadState()["seller"]
    print("Конечно, вот что у меня есть (введите название предмета или 'уйти')")
    PrintItems(LoadItems(merchant["items"]))
    return input().lower().strip()

def PrintItemsToSell():
    character = LoadState()["character"]
    print("Введите название предмета, который вы хотите продать или 'уйти'")
    PrintItems(LoadItems(character["items"]))
    return input().lower().strip()

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
   

def PrintBuyCompleted(item):
    print(f"Вы успешно приобрели {item}")

def PrintEnemyDead(character, enemy):
    message = f"{enemy["name"]} не сдержал вашего настиска и помер, "
    
    if(enemy["items"]):
        message += "оставив после себя "
        for item in enemy["items"]:
            message += item + ", "
            for equipment in character["items"]:
                if(equipment == item):
                    message += "(но у вас такой уже есть) "                
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
     
    message = f"{enemy["name"]} атаковал вас на {enemy["damage"]} урона, оставив вам {hp} здоровья"
    if(character["armor"] > 0):
        message += f" и {character["armor"]} брони"
    
    print(message)

def PrintCharacterDead():
    print(f"Герой умер")
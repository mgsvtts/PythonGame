from Infrastructure.config_loader import load_items, load_state
import Infrastructure

def print_menu():
    print("1 - ринуться в атаку")
    print("2 - найти ближайшего торговца")
    print("3 - посмотреть на себя красивого")
    print("4 - закончить игру")
    print("Выбери действие: ")
    return int(input())

def print_items(items):
    for item in items:
        print(f"- {item["name"]}")
        print(f"    цена {item["cost"]}")
        print(f"    урон {item["damage"]}")
        print(f"    защита {item["hp"]}")

def print_stats():
    character = load_state()["character"]
    equipments = load_items(character["items"])
    damage = character["damage"] + Infrastructure.Handlers.AttackHandler.CalculateDamage()

    print("=" * 30)
    print(f"Ваше имя: {character["name"]} и вы великий воин")
    print(f"Броня: {character["armor"]}")
    print(f"Здоровье {character["hp"]} из {character["maxHp"]}")
    print(f"Врожденный урон {character["damage"]}")
    print(f"Урон с надетым снаряжением {damage}")
    print(f"Червонцы {character["money"]}")
    print("Инвентарь:")
    print_items(equipments)
    print("=" * 30)

def print_already_has_item():
    print("У вас уже есть этот предмет")

def print_character_not_enough_money():
    print("К сожалению, у тебя не хватает денег")

def print_merchant_not_enough_money(character):
    print(f"Извини, {character["name"]}, но твой предмет слишком дорогой для меня")

def print_sell_completed(character):
    print(f"Конечно, {character}, я с радостью куплю у тебя это")

def print_merchant_found():
    merchant = load_state()["seller"]
    print(f"Привет, я {merchant["name"]}, что бы вы хотели?")
    print("1 - купить")
    print("2 - продать")
    print("3 - лечение (5 монет за 1 hp)")
    print("4 - ремонт (2 монеты за 1 броню)")
    print("5 - уйти")
    return int(input())

def print_merchant_items():
    merchant = load_state()["seller"]
    print("Конечно, вот что у меня есть (введите название предмета или 'уйти')")
    print_items(load_items(merchant["items"]))
    return input().lower().strip()

def print_items_to_sell():
    character = load_state()["character"]
    print("Введите название предмета, который вы хотите продать или 'уйти'")
    print_items(load_items(character["items"]))
    return input().lower().strip()

def print_enemy_found(enemy):
    print(f"На пути вам попался {enemy["name"]}")
    
def print_dice_result(dice):
    print(f"Вам выпало {dice}")
    
def print_enemy_attack_result(enemy, damage):
    if(enemy["hp"]<=0):
        hp = 0
    else:
        hp = enemy["hp"]
    
    print(f"Вы нанесли {damage} урона")
    print(f"У {enemy["name"]} осталось {hp} здоровья")
   

def print_buy_completed(item):
    print(f"Вы успешно приобрели {item}")

def print_enemy_dead(character, enemy):
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
   
def print_damage_taken(character, enemy):
    if(character["hp"] <=0):
        hp = 0
    else:
        hp = character["hp"]
     
    message = f"{enemy["name"]} атаковал вас на {enemy["damage"]} урона, оставив вам {hp} здоровья"
    if(character["armor"] > 0):
        message += f" и {character["armor"]} брони"
    
    print(message)

def print_character_dead():
    print(f"Герой умер")
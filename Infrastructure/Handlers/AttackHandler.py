import random
from Infrastructure.ConfigLoader import LoadConfig, LoadItems
from Infrastructure.Printer import PrintDamageTaken, PrintEnemyAttackResult, PrintEnemyDead, PrintEnemyFound


def FindRandomEnemy():
    enemies =  LoadConfig()["enemy"]
    
    enemy = random.choice(enemies)
    
    PrintEnemyFound(enemy)
    
    return enemy

def TryKillEnemy(enemy, character):
    damage = character["damage"] + CalculateDamage();
    enemy["hp"] -= damage
    
    PrintEnemyAttackResult(enemy, damage)

    if(enemy["hp"]>0):
        return False
    
    PrintEnemyDead(enemy)

    character["money"] += enemy["money"]
    if(enemy["items"]):
        character["items"] += enemy["items"]
    
    return True
    
def TryDie(enemy, character):
    character["hp"] -= enemy["damage"]
    
    PrintDamageTaken(character, enemy)
    
    if(character["hp"] > 0):
        return False
    
    return True

def CalculateArmor():
    equipment = LoadItems(LoadConfig()["character"]["items"])
    armorDict = {}
    for item in equipment:
        name = item["name"]
        if(name not in armorDict):
            armorDict[name] = item["hp"]
        
    return sum(armorDict.values())

def CalculateDamage():
    equipment = LoadItems(LoadConfig()["character"]["items"])
    damage = 0
    for item in equipment:
        damage += item["damage"]
        
    return damage

def HandleAttack():
    enemy = FindRandomEnemy()
    character = LoadConfig()["character"]
    character["hp"] += CalculateArmor()
    
    somebodyDied = False
    while(somebodyDied == False):
        dice = random.randint(1,6)
        if(dice > 3):
            somebodyDied = TryKillEnemy(enemy, character)
        else:
            somebodyDied = TryDie(enemy, character)
            
    
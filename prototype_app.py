from fighter import Fighter, DamageData
import json

class App:
    def __init__(self):
        pass

    def loadFighterData(self, index):
        with open("fighterList.json", "r") as file:
            data = json.load(file)
        fighterData = data.get("fighters", [])[index]
        return Fighter(
            name=fighterData['name'],
            health=fighterData['health'],
            maxHealth=fighterData['health'],
            mana=fighterData['mana'],
            maxMana=fighterData['mana'],
            strength=fighterData['strength'],
            intelligence=fighterData['intelligence'],
            defense=fighterData['defense'],
            spirit=fighterData['spirit'],
            accuracy=fighterData['accuracy'],
            agility=fighterData['agility'],
            criticalChance=fighterData['criticalChance'],
            criticalDamage=fighterData['criticalDamage'],
            manaRegen=fighterData['manaRegen']
        )

if __name__ == "__main__":
    app = App()
    # fighter1 = Fighter(name="Hero", health=100, maxHealth=100, mana=30, maxMana=30, attackPower=30, defense=30, criticalChance=15, criticalDamage=100, agility=5, accuracy=90)
    # fighter2 = Fighter(name="Dummy", health=100, maxHealth=100, mana=30, maxMana=30, attackPower=30, defense=30, criticalChance=15, criticalDamage=100, agility=5, accuracy=90)
    # damageData = fighter1.basicAttack(fighter2)
    # print(f"Target:{fighter2.name}, damage:{damageData.damage}, isCrit:{damageData.isCrit}, isMiss:{damageData.isMiss}")
    # fighter2.print()
    fighter1 = app.loadFighterData(0)
    fighter2 = app.loadFighterData(4)

    for x in range(12):
        fighter1.print()
        fighter2.print()

        damageData = fighter1.basicMagicAttack(fighter2)
        fighter2.checkAlive()
        print(damageData)
        if fighter2.getDeadFlag() == True:
            print(f"{fighter1.name} Win!")
            break
        damageData = fighter2.basicMagicAttack(fighter1)
        fighter1.checkAlive()
        print(damageData)
        if fighter1.getDeadFlag() == True:
            print(f"{fighter2.name} Win!")
            break

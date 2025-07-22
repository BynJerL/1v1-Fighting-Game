from fighter import Fighter, DamageData
import json

class App:
    def __init__(self):
        self.playedFighter = None

    def loadFighterData(self, index):
        with open("fighterList.json", "r") as file:
            data = json.load(file)
        fighterData = data.get("fighters", [])[index]
        self.playedFighter = Fighter(
            name=fighterData['name'],
            health=fighterData['health'],
            maxHealth=fighterData['health'],
            mana=fighterData['mana'],
            maxMana=fighterData['mana'],
            attackPower=fighterData['attackPower'],
            defense=fighterData['defense'],
            accuracy=fighterData['accuracy'],
            agility=fighterData['agility'],
            criticalChance=fighterData['criticalChance'],
            criticalDamage=fighterData['criticalDamage']
        )

if __name__ == "__main__":
    app = App()
    # fighter1 = Fighter(name="Hero", health=100, maxHealth=100, mana=30, maxMana=30, attackPower=30, defense=30, criticalChance=15, criticalDamage=100, agility=5, accuracy=90)
    # fighter2 = Fighter(name="Dummy", health=100, maxHealth=100, mana=30, maxMana=30, attackPower=30, defense=30, criticalChance=15, criticalDamage=100, agility=5, accuracy=90)
    # damageData = fighter1.basicAttack(fighter2)
    # print(f"Target:{fighter2.name}, damage:{damageData.damage}, isCrit:{damageData.isCrit}, isMiss:{damageData.isMiss}")
    # fighter2.print()
    app.loadFighterData(4)
    app.playedFighter.print()
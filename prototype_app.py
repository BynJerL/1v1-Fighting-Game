from fighter import Fighter, DamageData

class App:
    def __init__(self):
        pass

if __name__ == "__main__":
    app = App()
    fighter1 = Fighter(name="Hero", health=100, mana=30, attackPower=30, defense=30, criticalChance=15, criticalDamage=100)
    fighter2 = Fighter(name="Dummy", health=100, mana=30, attackPower=30, defense=3000, criticalChance=15, criticalDamage=100)
    damageData = fighter1.basicAttack(fighter2)
    print(f"Target:{fighter2.name}, damage:{damageData.damage}, isCrit:{damageData.isCrit}")
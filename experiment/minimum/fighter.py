import random as rd

class Fighter:
    def __init__(self, 
                 name: str, 
                 currHp: int, 
                 maxHp: int, 
                 currMana: int, 
                 maxMana: int, 
                 strength: int, 
                 defense: int,
                 skills: list["Skill"] = None):
        self.name = name
        self.currHp = currHp
        self.maxHp = maxHp
        self.currMana = currMana
        self.maxMana = maxMana
        self.strength = strength
        self.defense = defense

        self.isGuarded = False
        self.skills = skills if skills is not None else []
    
    @property
    def isAlive(self):
        return self.currHp > 0
    
    @property
    def getHpStatus(self):
        return f"{self.currHp}/{self.maxHp}"
    
    @property
    def getManaStatus(self):
        return f"{self.currMana}/{self.maxMana}"
    
    def adjustHp(self, amount):
        self.currHp = max(0, min(self.maxHp, self.currHp + amount))
    
    def adjustMana(self, amount):
        self.currMana = max(0, min(self.maxMana, self.currMana + amount))
    
    def enableGuard(self):
        self.isGuarded = True
    
    def disableGuard(self):
        self.isGuarded = False
    
    def takeDamage(self, amount):
        self.adjustHp(amount=-amount)
    
    def heal(self, amount):
        self.adjustHp(amount=amount)
    
    def useMana(self, amount):
        self.adjustMana(amount=-amount)
    
    def restoreMana(self, amount):
        self.adjustMana(amount=amount)

    def isManaAvailable(self, amount):
        return self.currMana >= amount

    def attack(self, target: "Fighter"):
        if not self.isAlive:
            raise ValueError(f"Cannot attack {target.name}, fighter is not alive.")
        
        damage = self.strength - target.defense
        if damage < 0:
            damage = 0
        
        target.takeDamage(damage)
        return damage

class Skill:
    def __init__(self,
                 name: str,
                 manaCost: int,
                 damageFunction: callable):
        self.name = name
        self.manaCost = manaCost
        self.damageFunction = damageFunction
    
    def use(self, user: Fighter, target: Fighter):
        if not user.isManaAvailable(self.manaCost):
            raise ValueError(f"{user.name} does not have enough mana to use {self.name}.")
        
        user.useMana(self.manaCost)
        rawDamage = self.damageFunction(user, target)
        netDamage = max(0, round(rawDamage - target.defense))
        target.takeDamage(netDamage)
        return netDamage

class Battle:
    def __init__(self, fighter1: Fighter, fighter2: Fighter):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.turn = 0
        self.winner = None
    
    @property
    def isOngoing(self):
        return self.fighter1.isAlive and self.fighter2.isAlive
    
    def next_turn(self):
        if self.isOngoing:
            attacker = self.fighter1 if self.turn % 2 == 0 else self.fighter2
            defender = self.fighter2 if attacker == self.fighter1 else self.fighter1
            
            if attacker.isManaAvailable(attacker.skills[0].manaCost):
                # Use the first skill for simplicity
                damage = attacker.skills[0].use(attacker, defender)
                print(f"{attacker.name} (HP: {attacker.getHpStatus}, SP: {attacker.getManaStatus}) used {attacker.skills[0].name} on {defender.name} dealing {damage} damage!")
            else:
                # Example attack
                attackDamage = attacker.attack(defender)
                print(f"{attacker.name} (HP: {attacker.getHpStatus}, SP: {attacker.getManaStatus}) dealt {attackDamage * -1} HP to {defender.name}!")
            
            if not defender.isAlive:
                self.winner = attacker
                print(f"{attacker.name} wins!")
            
            self.turn += 1
        else:
            print("Battle has ended.")

FIGHTERS = [
    Fighter(name="Warrior", currHp=100, maxHp=100, currMana=50, maxMana=50, strength=20, defense=10,
             skills=[Skill(name="Gale Slash", manaCost=10, damageFunction=lambda u, t: u.strength * 2)]),
    Fighter(name="Mage", currHp=80, maxHp=80, currMana=100, maxMana=100, strength=10, defense=5,
             skills=[Skill(name="Fireball", manaCost=20, damageFunction=lambda u, t: u.strength * 3)]),
    Fighter(name="Rogue", currHp=90, maxHp=90, currMana=60, maxMana=60, strength=15, defense=8,
             skills=[Skill(name="Backstab", manaCost=15, damageFunction=lambda u, t: u.strength * 2.5)]),
]

# Example usage
if __name__ == "__main__":
    battle = Battle(fighter1=FIGHTERS[0], fighter2=FIGHTERS[1])
    
    while battle.isOngoing:
        battle.next_turn()
    
    if battle.winner:
        print(f"The winner is {battle.winner.name}!")
    else:
        print("The battle ended in a draw.")
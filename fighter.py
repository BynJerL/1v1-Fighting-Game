import random as rd
from dataclasses import dataclass

@dataclass
class DamageData:
    """
    An object that used to store damage data from performed attack.
    
    Attributes
    ----------
    damage: int
        total damage caused by the attack.
    isCrit: bool
        critical hit status.
    isMiss: bool
        missing hit status.
    """
    damage: int
    isCrit: bool
    isMiss: bool

class Fighter:
    """
    An object that handles fighter data and actions.
    """
    def __init__(self, name: str, health: int, mana: int, attackPower: int, defense: int, accuracy: int, agility: int, criticalChance: float, criticalDamage: float) -> None:
        """
        The constructor of `Fighter` object.
        
        Parameters
        ----------
        `name` : str
            name of the fighter.
        `health` : int
            health of the fighter.
        `mana` : int
            mana capacity of the fighter.
        `attackPower` : int
            attack power of the fighter.
        `defense` : int
            defense of the fighter.
        `accuracy`: int
            attack accuracy of the fighter.
        `agility` : int
            agility of the fighter.
        `criticalChance` : float
            percentage of chance of critical hit when fighter do attack.
        `criticalDamage` : float
            percentage of additional damage when fighter dealt critical hit.
        """
        if len(name) < 0:
            raise ValueError(f"cannot insert empty name.")
        if health < 0:
            raise ValueError(f"health must be not less than 0. Got {health}")
        if mana < 0:
            raise ValueError(f"mana must be not less than 0. Got {mana}")
        if attackPower < 0:
            raise ValueError(f"attackPower must be not less than 0. Got {attackPower}")
        if defense < 0:
            raise ValueError(f"defense must be not less than 0. Got {defense}")
        if accuracy < 0:
            raise ValueError(f"accuracy must be not less than 0. Got {accuracy}")
        if agility < 0:
            raise ValueError(f"agility must be not less than 0. Got {agility}")
        if criticalChance < 0:
            raise ValueError(f"criticalChance must be not less than 0. Got {criticalChance}")
        if criticalDamage < 0:
            raise ValueError(f"criticalDamage must be not less than 0. Got {criticalDamage}")

        self.name = name
        self.currHealth = health
        self.maxHealth = health
        self.currMana = mana
        self.maxMana = mana
        self.attackPower = attackPower
        self.defense = defense
        self.accuracy = accuracy
        self.agility = agility
        self.criticalChance = criticalChance
        self.criticalDamage = criticalDamage

        self.isGuard = False
    
    def isAlive(self) -> bool:
        """
        Check if the fighter's is alive or not.

        Returns
        ------- 
        bool 
            player life status. 
        """
        return self.currHealth > 0
    
    def rollCrit(self) -> bool:
        """
        (Use when attacking) check if the fighter dealt critical hit or not.

        Returns
        -------
        bool
            critical hit status.
        """
        return rd.random() * 100 < self.criticalChance
    
    def rollMiss(self) -> bool:
        """
        (Use when being attacked) check if the fighter can evade incoming attack.

        Returns
        -------
        bool
            missing hit status.
        """
        divisor = self.accuracy + self.agility

        if divisor == 0:
            return True
        
        hitChance = self.accuracy / divisor
        return rd.random() > hitChance

    def changeHealth(self, amount: int) -> None:
        """
        Change fighter health by `amount`.

        Parameters
        ----------
        `amount`: int
            Amount of change. 
            Positive integer for increasing fighter's health; 
            Negative integer for decreasing fighter's health.
        """
        # Notes: Fighter health cannot exceed the `maxHealth` and cannot be less than `0`.
        self.currHealth = min(max(0, self.currHealth + amount), self.maxHealth)
    
    def takeDamage(self, amount: int) -> None:
        """
        Change fighter's health by negative value of `amount`, which resembles damage to fighter's health.

        Parameters
        ----------
        `amount`: int
            Amount of damage.
        """
        self.changeHealth(amount=-amount)
    
    def heal(self, amount: int) -> None:
        """
        Change fighter's health by positive value of `amount`, which resembles restoration of fighter's health.
        
        Parameters
        ----------
        `amount`: int
            Amount of heal.
        """
        self.changeHealth(amount=amount)
    
    def basicAttack(self, target: "Fighter") -> DamageData:
        """
        Perform basic attack to another fighter.

        Parameters
        ----------
        `target`: Fighter
            target of your attack.
        """
        isMiss = target.rollMiss()
        isCrit = self.rollCrit() if not isMiss else False
        if not isMiss:
            rawDamage = self.attackPower * (1 + 0.01 * isCrit * self.criticalDamage)
            netDamage = max(0, round(rawDamage - (0.2 + 0.5 * target.isGuard) * target.defense))
            target.takeDamage(netDamage)
        else:
            netDamage = 0

        damageData = DamageData(damage=netDamage, isCrit=isCrit, isMiss=isMiss)
        return damageData
    
    def enableGuard(self) -> None:
        """
        Enable guard status.
        """
        self.isGuard = True
    
    def disableGuard(self) -> None:
        """
        Disable guard status.
        """
        self.isGuard = False
import random as rd
from dataclasses import dataclass

@dataclass
class DamageData:
    """
    An object that used to store damage data from performed attack.
    
    Attributes
    ----------
    `damage`: int
        total damage caused by the attack.
    `isCrit`: bool
        critical hit status.
    `isMiss`: bool
        missing hit status.
    """
    damage: int
    isCrit: bool
    isMiss: bool

class Fighter:
    """
    An object that handles fighter data and actions.
    """
    def __init__(self, name: str, health: int, maxHealth: int, mana: int, maxMana: int, strength: int, intelligence: int, defense: int, spirit: int, accuracy: int, agility: int, criticalChance: float, criticalDamage: float, manaRegen: int) -> None:
        """
        The constructor of `Fighter` object.
        
        Parameters
        ----------
        `name` : str
            name of the fighter.
        `health` : int
            health of the fighter.
        `maxHealth` : int
            maximum health of the fighter.
        `mana` : int
            mana capacity of the fighter.
        `maxMana` : int
            maximum mana capacity of the fighter.
        `strength` : int
            strength of the fighter.
        `intelligence`: int
            intelligence of the fighter.
        `defense` : int
            defense of the fighter.
        `spirit` : int
            spiritual defense of the fighter.
        `accuracy`: int
            attack accuracy of the fighter.
        `agility` : int
            agility of the fighter.
        `criticalChance` : float
            percentage of chance of critical hit when fighter do attack.
        `criticalDamage` : float
            percentage of additional damage when fighter dealt critical hit.
        `manaRegen` : int
            mana regeneration power of the fighter.
        """
        if len(name) == 0:
            raise ValueError(f"cannot insert empty name.")
        if health < 0:
            raise ValueError(f"health must be not less than 0. Got {health}")
        if maxHealth < 0:
            raise ValueError(f"maxHealth must be not less than 0. Got {maxHealth}")
        if mana < 0:
            raise ValueError(f"mana must be not less than 0. Got {mana}")
        if maxMana < 0:
            raise ValueError(f"maxMana must be not less than 0. Got {maxMana}")
        if strength < 0:
            raise ValueError(f"strength must be not less than 0. Got {strength}")
        if intelligence < 0:
            raise ValueError(f"intelligence must be not less than 0. Got {intelligence}")
        if defense < 0:
            raise ValueError(f"defense must be not less than 0. Got {defense}")
        if spirit < 0:
            raise ValueError(f"spirit must be not less than 0. Got {spirit}")
        if accuracy < 0:
            raise ValueError(f"accuracy must be not less than 0. Got {accuracy}")
        if agility < 0:
            raise ValueError(f"agility must be not less than 0. Got {agility}")
        if criticalChance < 0:
            raise ValueError(f"criticalChance must be not less than 0. Got {criticalChance}")
        if criticalDamage < 0:
            raise ValueError(f"criticalDamage must be not less than 0. Got {criticalDamage}")
        if manaRegen < 0:
            raise ValueError(f"manaRegen must be not less than 0. Got {manaRegen}")

        self.name = name
        self.currHealth = health
        self.maxHealth = maxHealth
        self.currMana = mana
        self.maxMana = maxMana
        self.strength = strength
        self.intelligence = intelligence
        self.defense = defense
        self.spirit = spirit
        self.accuracy = accuracy
        self.agility = agility
        self.criticalChance = criticalChance
        self.criticalDamage = criticalDamage
        self.manaRegen = manaRegen

        self.__isGuard = False
        self.__isDead = False

    @property
    def health(self) -> int:
        """
        current health point of the fighter.
        """
        return self.currHealth
    
    @property
    def mana(self) -> int:
        """
        current mana point of the fighter.
        """
        return self.currMana
    
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
    
    def rollMiss(self, attacker: "Fighter") -> bool:
        """
        (Use when being attacked) check if the fighter can evade incoming attack.

        Parameters
        ----------
        `self`: Fighter
            defender fighter.
        `attacker`: Fighter
            attacker fighter.

        Returns
        -------
        bool
            missing hit status.
        """
        divisor = attacker.accuracy + self.agility

        if divisor == 0:
            return True
        
        hitChance = attacker.accuracy / divisor
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
    
    def changeMana(self, amount: int) -> None:
        """
        Change fighter's mana by `amount`

        Parameters
        ----------
        `amount`: int
            Amount of change.
            Positive integer for increasing fighter's mana;
            Negative integer for decreasing fighter's mana.
        """
        # Notes: Fighter's mana is also cannot exceed `maxMana` and cannot be less than `0`.
        changedMana = self.currMana + amount
        if changedMana < 0:
            raise ValueError("amount cannot be greater than current mana!")
        
        self.currMana = min(changedMana, self.maxMana)

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

    def hasEnoughMana(self, cost: int) -> bool:
        """
        Check if the fighter's mana is enough for performing a skill.

        Parameters
        ----------
        `cost`: int
            mana cost of the skill.
        """
        return self.currMana >= cost
    
    def consumeMana(self, amount: int) -> None:
        """
        decrease fighter's mana by `amount`.

        Parameter
        ---------
        `amount`: int
            amount of mana consumption.
        """
        self.changeMana(amount=-amount)
    
    def restoreMana(self, amount: int) -> None:
        """
        increase fighter's mana by `amount`

        Parameters
        ----------
        `amount`: int
            amount of mana restoration.
        """
        self.changeMana(amount=amount)
    
    def passiveManaRegen(self):
        """
        Regenerates mana based on mana regeneration power.
        """
        self.restoreMana(self.manaRegen)

    def basicAttack(self, target: "Fighter") -> DamageData:
        """
        Perform basic attack to another fighter.

        Parameters
        ----------
        `target`: Fighter
            target of your attack.
        """
        # Note: For now, the basic attack are using strength and not intelligence; defense and not spirit.
        isMiss = target.rollMiss(attacker=self)
        isCrit = self.rollCrit() if not isMiss else False
        if not isMiss:
            rawDamage = self.strength * (1 + 0.01 * isCrit * self.criticalDamage)
            netDamage = max(0, round(rawDamage - target.getDefenseFactor() * target.defense))
            target.takeDamage(netDamage)
        else:
            netDamage = 0

        damageData = DamageData(damage=netDamage, isCrit=isCrit, isMiss=isMiss)
        return damageData
    
    def enableGuard(self) -> None:
        """
        Enable guard status.
        """
        self.__isGuard = True
    
    def disableGuard(self) -> None:
        """
        Disable guard status.
        """
        self.__isGuard = False
    
    def checkAlive(self) -> None:
        """
        Check the player life flag status.
        """
        if not self.isAlive():
            self.__isDead = True
    
    def getDeadFlag(self) -> bool:
        """
        Get the fighter's life flag status.
        """
        return self.__isDead
    
    def getDefenseFactor(self) -> bool:
        """
        Get the fighter's defense factor.
        """
        return 0.7 if self.__isGuard else 0.2

    def print(self) -> None:
        print(self)

    def __str__(self) -> str:
        """
        Get string representation of the object

        Returns
        -------
        `str`
            string representation of the fighter object.
        """
        return (
            f"{self.name} [HP: {self.currHealth}/{self.maxHealth}, "
            f"Mana: {self.currMana}/{self.maxMana}, "
            f"ATK: {self.strength}|{self.intelligence}, DEF: {self.defense}|{self.spirit}, "
            f"CRIT: {self.criticalChance:.1f}% (+{self.criticalDamage:.1f}%), "
            f"ACR: {self.accuracy}, AGI: {self.agility}, MREG: {self.manaRegen}]"
        )
    
    def __repr__(self) -> str:
        """
        Clean view for developer.
        """
        return f"Fighter(name={self.name}, health={self.currHealth}/{self.maxHealth})"
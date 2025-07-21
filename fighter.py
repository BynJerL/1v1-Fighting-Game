import random as rd

class Fighter:
    """
    An object that handles fighter data and actions.
    """
    def __init__(self, name: str, health: int, mana: int, attackPower: int, defense: int, criticalChance: float, criticalDamage: float) -> None:
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
        `criticalChance` : float
            percentage of chance of critical hit when fighter do attack.
        `criticalDamage` : float
            percentage of additional damage when fighter dealt critical hit.
        """
        self.name = name
        self.currHealth = health
        self.maxHealth = health
        self.currMana = mana
        self.maxMana = mana
        self.attackPower = attackPower
        self.defense = defense
        self.criticalChance = criticalChance
        self.criticalDamage = criticalDamage
    
    def isAlive(self) -> bool:
        """
        Check if the fighter's is alive or not.

        Returns
        ------- 
        bool 
            player life status. 
        """
        return self.currHealth > 0
    
    def isCrit(self) -> bool:
        """
        (Use when attacking) check if the fighter dealt critical hit or not.

        Returns
        -------
        bool
            critical hit status.
        """
        return rd.random() * 100 < self.criticalChance
    
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
class Fighter:
    def __init__(self, name: str, health: int, mana: int, attackPower: int, defense: int, criticalChance: float, criticalDamage: float) -> None:
        """
        An object that handles fighter data and actions.
        
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
            chance of critical hit when fighter do attack (in-percentage).
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
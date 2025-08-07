import random as rd
from equipment import Equipment

class Fighter:
    def __init__(self,
                 name: str,
                 currHp: int,
                 maxHp: int,
                 currEn: int,
                 maxEn: int,
                 currMana: int,
                 maxMana: int,
                 currBurst: float,
                 energyRegen: float,
                 manaRegen: float,
                 burstGain: float,
                 strength: int,
                 intelligence: int,
                 armor: int,
                 spirit: int,
                 accuracy: int,
                 evasion: int,
                 speed: int,
                 critChance: float,
                 critDamage: float,
                 equipments: dict = {
                     'head': None,
                     'torso': None,
                     'hand': None,
                     'foot': None,
                     'acc_1': None,
                     'acc_2': None
                 },
                 skills: list = [],
                 statuses: list = []):
        self.name = name
        self.currHp = currHp
        self.maxHp = maxHp
        self.currEn = currEn
        self.maxEn = maxEn
        self.currMana = currMana
        self.maxMana = maxMana
        self.currBurst = currBurst
        self.energyRegen = energyRegen
        self.manaRegen = manaRegen
        self.burstGain = burstGain
        self.strength = strength
        self.intelligence = intelligence
        self.armor = armor
        self.spirit = spirit
        self.accuracy = accuracy
        self.evasion = evasion
        self.speed = speed
        self.critChance = critChance
        self.critDamage = critDamage
        
        self.equipments = equipments
        self.skills = skills
        self.statuses = statuses

        self.isGuarded = False
    
    def getHpStatus(self) -> str:
        return f"{self.currHp}/{self.maxHp}"
    
    def getEnStatus(self) -> str:
        return f"{self.currEn}/{self.maxEn}"
    
    def getManaStatus(self) -> str:
        return f"{self.currMana}/{self.maxMana}"
    
    def getBurstStatus(self) -> str:
        return f"{self.currBurst}%"
    
    @property
    def isAlive(self) -> bool:
        return self.currHp > 0
    
    def gainHp(self, amount: int) -> None:
        self.currHp = max(0, min(self.maxHp, self.currHp + amount))
    
    def loseHp(self, amount: int) -> None:
        self.currHp = max(0, min(self.currHp - amount, self.maxHp))
    
    def gainEn(self, amount: int) -> None:
        self.currEn = max(0, min(self.maxEn, self.currEn + amount))
    
    def loseEn(self, amount: int) -> None:
        self.currEn = max(0, min(self.currEn - amount, self.maxEn))
    
    def gainMana(self, amount: int) -> None:
        self.currMana = max(0, min(self.maxMana, self.currMana + amount))
    
    def loseMana(self, amount: int) -> None:
        self.currMana = max(0, min(self.currMana - amount, self.maxMana))
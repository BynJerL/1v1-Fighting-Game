import random as rd
from equipment import Equipment, EquipmentCategory

MAX_HP_CAP = 999_999
MAX_EN_CAP = 999
MAX_MANA_CAP = 999

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
                 equipments: dict[str, Equipment] = None,
                 skills: list = [],
                 statuses: list = []):
        if len(name) == 0:
            raise ValueError(f"Cannot insert empty name.")
        _validate_stat(name="maxHp", value=maxHp, max_val=MAX_HP_CAP)
        _validate_stat(name="currHp", value=currHp, max_val=maxHp)
        _validate_stat(name="maxEn", value=maxEn, max_val=MAX_EN_CAP)
        _validate_stat(name="currEn", value=currEn, max_val= maxEn)
        _validate_stat(name="maxMana", value=maxMana, max_val=MAX_MANA_CAP)
        _validate_stat(name="currMana", value=currMana, max_val= maxMana)
        _validate_stat(name="currBurst", value=currBurst, min_val=0.0, max_val=100.0)
        _validate_stat(name="energyRegen", value=energyRegen, min_val=0.0)
        _validate_stat(name="manaRegen", value=manaRegen, min_val=0.0)
        _validate_stat(name="burstGain", value=burstGain, min_val=0.0)
        _validate_stat(name="strength", value=strength, min_val=0)
        _validate_stat(name="intelligence", value=intelligence, min_val=0)
        _validate_stat(name="armor", value=armor, min_val=0)
        _validate_stat(name="spirit", value=spirit, min_val=0)
        _validate_stat(name="accuracy", value=accuracy, min_val=0)
        _validate_stat(name="evasion", value=evasion, min_val=0)
        _validate_stat(name="speed", value=speed, min_val=0)
        _validate_stat(name="critChance", value=critChance, min_val=0.0, max_val=1.0)
        _validate_stat(name="critDamage", value=critDamage, min_val=0.0)
        
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
        
        self.equipments = equipments or {
            'head': None,
            'torso': None,
            'hand': None,
            'foot': None,
            'acc_1': None,
            'acc_2': None
        }
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
    
    def getStats(self, statName: str):
        baseValue = getattr(self, statName, 0)
        bonus = 0

        for equipment in self.equipments.values():
            if isinstance(equipment, Equipment):
                bonus += equipment.effectBonus.get(statName, 0)
        
        return baseValue + bonus
    
    def rollCrit(self) -> bool:
        return rd.random() < self.getCritChance()
    
    def rollHit(self, target: "Fighter") -> bool:
        divisor = self.getAccuracy() + target.getEvasion()

        if divisor == 0:
            return False
        
        hitChance = self.getAccuracy() / divisor
        return rd.random() < hitChance

    def getStrength(self) -> int:
        return self.getStats("strength")
    
    def getIntelligence(self) -> int:
        return self.getStats("intelligence")
    
    def getArmor(self) -> int:
        return self.getStats("armor")
    
    def getSpirit(self) -> int:
        return self.getStats("spirit")
    
    def getSpeed(self) -> int:
        return self.getStats("speed")
    
    def getAccuracy(self) -> int:
        return self.getStats("accuracy")
    
    def getEvasion(self) -> int:
        return self.getStats("evasion")
    
    def getCritChance(self) -> float:
        return self.getStats("critChance")
    
    def getCritDamage(self) -> float:
        return self.getStats("critDamage")
    
def _validate_stat(name: str, value: int|float, min_val: int|float = 0, max_val: int|float = None):
    if value < min_val:
        raise ValueError(f"{name} must not be less than {min_val}. Got: {value}")
    if max_val is not None and value > max_val:
        raise ValueError(f"{name} must not be greater than {max_val}. Got: {value}")
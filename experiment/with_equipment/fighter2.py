import random as rd
from equipment import Equipment, EquipmentCategory

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
        if currHp < 0:
            raise ValueError(f"currHp must not be less than 0. Got: {currHp}")
        if maxHp < 0:
            raise ValueError(f"maxHp must not be less than 0. Got: {maxHp}")
        if currEn < 0:
            raise ValueError(f"currEn must not be less than 0. Got: {currEn}")
        if maxEn < 0:
            raise ValueError(f"maxEn must not be less than 0. Got: {maxEn}")
        if currMana < 0:
            raise ValueError(f"currMana must not be less than 0. Got: {currMana}")
        if maxMana < 0:
            raise ValueError(f"maxMana must not be less than 0. Got: {maxMana}")
        if currBurst < 0:
            raise ValueError(f"currBurst must not be less than 0. Got: {currBurst}")
        if energyRegen < 0:
            raise ValueError(f"energyRegen must not be less than 0. Got: {energyRegen}")
        if manaRegen < 0:
            raise ValueError(f"manaRegen must not be less than 0. Got: {manaRegen}")
        if burstGain < 0:
            raise ValueError(f"burstGain must not be less than 0. Got: {burstGain}")
        if strength < 0:
            raise ValueError(f"strength must not be less than 0. Got: {strength}")
        if intelligence < 0:
            raise ValueError(f"intelligence must not be less than 0. Got: {intelligence}")
        if armor < 0:
            raise ValueError(f"armor must not be less than 0. Got: {armor}")
        if spirit < 0:
            raise ValueError(f"spirit must not be less than 0. Got: {spirit}")
        if accuracy < 0:
            raise ValueError(f"accuracy must not be less than 0. Got: {accuracy}")
        if evasion < 0:
            raise ValueError(f"evasion must not be less than 0. Got: {evasion}")
        if speed < 0:
            raise ValueError(f"speed must not be less than 0. Got: {speed}")
        if critChance < 0:
            raise ValueError(f"critChance must not be less than 0. Got: {critChance}")
        if critDamage < 0:
            raise ValueError(f"critDamage must not be less than 0. Got: {critDamage}")
        
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
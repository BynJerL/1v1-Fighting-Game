from enum import Enum, auto

class EquipmentCategory(Enum):
    HEAD = auto()
    TORSO = auto()
    HAND = auto()
    FOOT = auto()
    ACCESSORY = auto()

class Equipment:
    def __init__(self,
                 name: str,
                 category: EquipmentCategory,
                 effectBonus: dict):
        self.name = name
        self.category = category
        self.effectBonus = effectBonus
    
    def __str__(self):
        return f"{self.name} ({self.category}) - Bonuses: {self.effectBonus}"
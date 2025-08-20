from enum import Enum, auto

class TargetType(Enum):
    SELF = auto()
    ALLY_ONE = auto()
    ENEMY_ONE = auto()
    ALLY_ALL = auto()
    ENEMY_ALL = auto()

class Skill:
    def __init__(self, name: str, manaCost: int, energyCost: int, formula: dict, targetType: TargetType, specialFlags: dict = None):
        self.name = name
        self.manaCost = manaCost
        self.energyCost = energyCost
        self.formula = formula
        self.targetType = targetType
        self.specialFlags = specialFlags or {}
    
    def execute(self, user, target):
        pass
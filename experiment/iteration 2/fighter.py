# Prototype for improvement
class Fighter:
    def __init__(self, 
                 name, 
                 currHp,
                 maxHp, 
                 currMana, 
                 maxMana,
                 manaRegen,
                 stamina,
                 intelligence,
                 armor,
                 spirit,
                 evasion,
                 accuracy,
                 speed,
                 critChance,
                 critDmg,
                 equipment = None,
                 skill = None):
        self.name = name
        self.currHp = currHp
        self.maxHp = maxHp
        self.currMana = currMana
        self.maxMana = maxMana
        self.manaRegen = manaRegen
        self.stamina = stamina
        self.intelligence = intelligence
        self.armor = armor
        self.spirit = spirit
        self.evasion = evasion
        self.accuracy = accuracy
        self.speed = speed
        self.critChance = critChance
        self.critDmg = critDmg
        self.equipment = equipment if not None else {
            "top": None,
            "body": None,
            "leg": None,
            "foot": None,
            "accecories": None
        }

        self.skill = skill if not None else {}
class Fighter:
    # Hp - Health Point
    # Mana - Used for performing a skill
    # Energy% - Power up (increase stats)
    # Burst% - Used for using signature move
    def __init__(self, 
                 name, 
                 currHp, 
                 maxHp, 
                 currMana, 
                 maxMana, 
                 currEn, 
                 currBurst,
                 manaRegen,
                 energyGain,
                 burstGain,
                 strength,
                 intelligence,
                 armor,
                 spirit,
                 accuracy,
                 evasion,
                 speed,
                 critChance,
                 critDamage,
                 equipments: dict = None,
                 skills: list = None,
                 statuses: list = None):
        self.name = name
        self.currHp = currHp
        self.maxHp = maxHp
        self.currMana = currMana
        self.maxMana = maxMana
        self.currEn = currEn
        self.currBurst = currBurst
        self.manaRegen = manaRegen
        self.energyGain = energyGain
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
        self.skills = skills or []
        self.statuses = statuses or []

        self.isGuarded = False
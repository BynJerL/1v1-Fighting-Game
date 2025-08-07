from equipment import EquipmentCategory, Equipment
from fighter2 import Fighter

characters = [
    Fighter(name="Hero", currHp=240, maxHp=240, currEn=35, maxEn=35, currMana=15, maxMana=15, currBurst=0, energyRegen=0.075, manaRegen=0.06, burstGain=12.5, strength=15, intelligence=10, armor=15, spirit=12, accuracy=94, evasion=10, speed=100, critChance=0.2, critDamage=0.75,
            equipments={
                'head': Equipment(name='Leather Helmet', category=EquipmentCategory.HEAD, effectBonus={
                    'armor': +4,
                }),
                'torso': Equipment(name='Leather Jacket', category=EquipmentCategory.TORSO, effectBonus={
                    'armor': +5,
                }),
                'hand': Equipment(name="Leather Gloves", category=EquipmentCategory.HAND, effectBonus={
                    'armor': +2,
                    'strength': +5
                }),
                'foot': Equipment(name="Leather Gloves", category=EquipmentCategory.FOOT, effectBonus={
                    'armor': +3,
                    'speed': +5
                }),
                'acc_1': None,
                'acc_2': None,
            }, skills=[]),
]

print(characters[0].equipments['hand'])
from equipment import EquipmentCategory, Equipment
from fighter2 import Fighter
from battle_manager import BattleManager

characters = [
    Fighter(name="Hero", currHp=240, maxHp=240, currEn=35, maxEn=35, currMana=15, maxMana=15, currBurst=0, energyRegen=0.075, manaRegen=0.06, burstGain=12.5, strength=42, intelligence=32, armor=15, spirit=12, accuracy=94, evasion=10, speed=100, critChance=0.2, critDamage=0.75,
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
    Fighter(name="Sidekick", currHp=240, maxHp=240, currEn=35, maxEn=35, currMana=15, maxMana=15, currBurst=0, energyRegen=0.075, manaRegen=0.06, burstGain=12.5, strength=36, intelligence=28, armor=15, spirit=12, accuracy=94, evasion=10, speed=110, critChance=0.2, critDamage=0.75,
            equipments={
                'head': Equipment(name='Leather Helmet', category=EquipmentCategory.HEAD, effectBonus={
                    'armor': +4,
                }),
                'torso': Equipment(name='Leather Jacket', category=EquipmentCategory.TORSO, effectBonus={
                    'armor': +5,
                }),
                'hand': Equipment(name="Apprentice Gloves", category=EquipmentCategory.HAND, effectBonus={
                    'armor': +4,
                    'strength': +8
                }),
                'foot': Equipment(name="Leather Gloves", category=EquipmentCategory.FOOT, effectBonus={
                    'armor': +3,
                    'speed': +5
                }),
                'acc_1': None,
                'acc_2': None,
            }, skills=[]),
]

# print(characters[0].getHpStatus())
# print(characters[0].getManaStatus())
# print(characters[0].getEnStatus())
# print(characters[0].equipments['torso'])
# print(characters[0].getStrength())
# print(characters[0].getIntelligence())
# print(characters[0].getArmor())
# print(characters[0].getSpirit())
# print(characters[0].getSpeed())
# print(characters[0].getAccuracy())
# print(characters[0].getEvasion())
# print(characters[0].getCritChance())
# print(characters[0].getCritDamage())

_BM = BattleManager(characters[0], characters[1])
_BM.startBattle()
# for fighter in _BM.currentQueue:
#     print(fighter.name)
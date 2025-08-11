from fighter2 import Fighter

class BattleManager:
    def __init__(self, playerFighter: Fighter, enemyFighter: Fighter):
        self.playerFighter = playerFighter
        self.enemyFighter = enemyFighter
        self.currentQueue = None
        self.roundCycle = 0
        self.actionCount = 0
        self.winner = None
    
    def startBattle(self, surprise_attacker = None):
        print("Battle Starts!")

        if surprise_attacker:
            print("--- Surprise Attack! ---")
            self.currentQueue = [surprise_attacker]
            self.roundCycle = 0
        else:
            self.currentQueue = self.rollTurn()
            self.roundCycle = 1
            print(f"--------- Round #{self.roundCycle} ----------")
        
        self.handleQueue()

    def handleQueue(self):
        while not self.winner:
            if not self.currentQueue:
                self.currentQueue = self.rollTurn()
                self.roundCycle += 1
                print(f"--------- Round #{self.roundCycle} ----------")

            attacker = self.currentQueue.pop(0)
            if not attacker.isAlive:
                continue

            # Placeholder
            defender = self.enemyFighter if attacker is self.playerFighter else self.playerFighter
            
            self.take_turn(attacker, defender)
            self.check_victory()

    def rollTurn(self):
        return sorted(
            [self.playerFighter, self.enemyFighter], 
            key=lambda f: f.speed,
            reverse=True
        )
    
    def take_turn(self, attacker: Fighter, defender: Fighter):
        self.actionCount += 1
        
        # placeholder for now :D
        basic_attack = {
            "name": "Hit!",
            "actionType": "attack",
            "attackType": "physical",
            "components": [
                {"stat": "strength", "multiplier": 1.0}
            ],
            "defenseStat": "armor",
            "ignoreDefense": False,
            "flatBonus": 0
        }

        if attacker.rollHit(defender):
            dmg = attacker.calculateDamage(target=defender, formula=basic_attack)
            isCrit = attacker.rollCrit()
            if isCrit:
                dmg = int(dmg * (1 + attacker.getCritDamage()))
            defender.loseHp(dmg)
            print(("(CRIT!) " if isCrit else "") + f"{attacker.name} ({attacker.getHpStatus()}) hits {defender.name} for {dmg} damage!")
        else:
            print(f"{attacker.name} ({attacker.getHpStatus()}) missed {defender.name}!")


    def check_victory(self):
        if not self.playerFighter.isAlive:
            self.winner = self.enemyFighter
        elif not self.enemyFighter.isAlive:
            self.winner = self.playerFighter
        
        if self.winner:
            print(f"*** {self.winner.name} wins! ***")
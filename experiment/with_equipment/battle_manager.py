from fighter2 import Fighter

class BattleManager:
    def __init__(self, playerFighter: Fighter, enemyFighter: Fighter):
        self.playerFighter = playerFighter
        self.enemyFighter = enemyFighter
        self.currentQueue = None
        self.nextQueue = None
        self.roundCycle = 0
        self.winner = None
class BattleManager:
    def __init__(self):
        self.currentQueue = None
        self.nextQueue = None
        self.roundCycle = 0
        self.winner = None
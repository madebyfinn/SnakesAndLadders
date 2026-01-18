# SnakesLadders
# ├── jumps            ← data (board layout)
# ├── play()           ← turn orchestration
# ├── bounce()         ← movement rule
# └── apply_jump()     ← board rule


import random
from ftplib import parse150
from wsgiref.util import application_uri


class SnakesLadders():
    jumps = {
        2:38,
        7:14,
        8:31,
        15:26,
        16:6,
        21:42,
        28:84,
        36:44,
        46:25,
        49:11,
        51:67,
        62:19,
        64:60,
        71:91,
        74:53,
        78:98,
        87:94,
        89:68,
        92:88,
        95:75,
        99:80
    }

    def __init__(self):
        self.p1_position = 0
        self.p2_position = 0
        self.current = 0

    def apply_jump(self, pos):
        if pos in self.jumps:
            return self.jumps[pos]
        return pos

    def play(self, die1, die2):
        if self.p1_position or self.p2_position == 100:
            return "Game over!"
        dice_total = die1 + die2
        if self.current == 0:
            pos = self.p1_position + dice_total
            pos = self.apply_jump(pos)
            self.p1_position = pos
            if die1 != die2:
                self.current = 1

        elif self.current == 1:
            pos = self.p2_position + dice_total
            self.p2_position = self.apply_jump(pos)
            if die1 != die2:
                self.current = 0

        else:
            return "Error: current player is unknown"




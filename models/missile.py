import numpy as np

class Missile:
    def __init__(self, position, speed, max_turn_rate):
        self.pos = np.array(position, dtype=float)
        self.heading = np.pi / 2
        self.speed = speed
        self.max_turn = max_turn_rate

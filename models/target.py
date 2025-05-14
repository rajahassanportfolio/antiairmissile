import numpy as np

class Target:
    def __init__(self, position, velocity):
        self.pos = np.array(position, dtype=float)
        self.vel = np.array(velocity, dtype=float)

    def update(self, dt):
        self.pos += self.vel * dt

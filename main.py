from models.missile import Missile
from models.target import Target
from guidance.proportional_nav import proportional_navigation
from plots.visualize import plot_trajectories
import config
import numpy as np

def main():
    dt = config.TIME_STEP
    t_total = config.TOTAL_TIME

    target = Target(config.TARGET_INIT_POS, config.TARGET_VELOCITY)
    missile = Missile(config.MISSILE_INIT_POS, config.MISSILE_SPEED, config.MAX_TURN_RATE)

    missile_trace, target_trace = [], []

    for t in np.arange(0, t_total, dt):
        target.update(dt)
        proportional_navigation(missile, target, config.NAV_CONSTANT, dt)

        missile_trace.append(missile.pos.copy())
        target_trace.append(target.pos.copy())

        if np.linalg.norm(missile.pos - target.pos) < config.HIT_DISTANCE:
            print(f"Intercepted at t={t:.2f}s at {missile.pos}")
            break

    plot_trajectories(missile_trace, target_trace)

if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
import numpy as np

def plot_trajectories(missile_trace, target_trace):
    missile = np.array(missile_trace)
    target = np.array(target_trace)

    plt.plot(missile[:,0], missile[:,1], label="Missile")
    plt.plot(target[:,0], target[:,1], label="Target")
    plt.scatter(missile[-1,0], missile[-1,1], color='red', label="Intercept")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.title("Missile Interception")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()

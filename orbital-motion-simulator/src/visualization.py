import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def plot_orbit(states):
    """Plot static 3D orbit."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(states[:, 0], states[:, 1], states[:, 2], label='Orbit')
    ax.scatter([0], [0], [0], color='blue', s=100, label='Earth')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    ax.legend()
    plt.show()

def animate_orbit(states):
    """Create 3D animation of orbit."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([0], [0], [0], color='blue', s=100, label='Earth')
    line, = ax.plot([], [], [], label='Orbit')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    ax.legend()

    def init():
        ax.set_xlim(np.min(states[:, 0]), np.max(states[:, 0]))
        ax.set_ylim(np.min(states[:, 1]), np.max(states[:, 1]))
        # Handle constant z-coordinates to avoid singular transformation
        z_min, z_max = np.min(states[:, 2]), np.max(states[:, 2])
        if z_min == z_max:
            z_min, z_max = z_min - 1e6, z_max + 1e6  # Add small range for 2D orbits
        ax.set_zlim(z_min, z_max)
        return line,

    def update(frame):
        line.set_data(states[:frame, 0], states[:frame, 1])
        line.set_3d_properties(states[:frame, 2])
        return line,

    ani = FuncAnimation(fig, update, frames=len(states), init_func=init, blit=True)
    plt.show()
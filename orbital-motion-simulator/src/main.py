import numpy as np
from physics import simulate_orbit
from visualization import plot_orbit, animate_orbit
from maneuvers import hohmann_transfer

def main():
    # Initial conditions: Earth orbit
    mu = 3.986e14  # Standard gravitational parameter for Earth (m^3/s^2)
    r0 = np.array([7000e3, 0, 0])  # Initial position (m)
    v0 = np.array([0, np.sqrt(mu / 7000e3), 0])  # Initial velocity (m/s)
    t_span = np.linspace(0, 2 * np.pi * np.sqrt((7000e3)**3 / mu), 1000)  # One orbit period

    # Simulate orbit
    states = simulate_orbit(r0, v0, t_span, mu)

    # Plot static orbit
    plot_orbit(states)

    # Animate orbit
    animate_orbit(states)

    # Perform Hohmann transfer to higher orbit (e.g., 10,000 km)
    r_target = 10000e3
    delta_v1, delta_v2 = hohmann_transfer(7000e3, r_target, mu)
    print(f"Hohmann Transfer: Δv1 = {delta_v1:.2f} m/s, Δv2 = {delta_v2:.2f} m/s")

if __name__ == "__main__":
    main()
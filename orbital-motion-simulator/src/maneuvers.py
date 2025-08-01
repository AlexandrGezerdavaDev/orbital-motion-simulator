import numpy as np

def hohmann_transfer(r1, r2, mu):
    """Calculate Δv for Hohmann transfer between circular orbits."""
    v1 = np.sqrt(mu / r1)  # Initial orbit velocity
    v2 = np.sqrt(mu / r2)  # Final orbit velocity
    v_transfer1 = np.sqrt(mu / r1) * (np.sqrt(2 * r2 / (r1 + r2)) - 1)  # Δv to enter transfer orbit
    v_transfer2 = np.sqrt(mu / r2) * (1 - np.sqrt(2 * r1 / (r1 + r2)))  # Δv to circularize at r2
    return v_transfer1, v_transfer2
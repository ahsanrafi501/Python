import matplotlib.pyplot as plt
import numpy as np

def projectile_motion(v0, theta, g=9.8, t_total=10, dt=0.01):
    """
    Simulate projectile motion and return the trajectory.

    Parameters:
    - v0: Initial velocity magnitude (m/s)
    - theta: Launch angle in degrees
    - g: Acceleration due to gravity (m/s^2), default is Earth's gravity
    - t_total: Total simulation time (s)
    - dt: Time step for simulation (s)

    Returns:
    - t_values: Time values
    - x_values: X-coordinate values
    - y_values: Y-coordinate values
    """

    # Convert angle to radians
    theta_rad = np.radians(theta)

    # Initial velocity components
    vx0 = v0 * np.cos(theta_rad)
    vy0 = v0 * np.sin(theta_rad)

    # Time values
    t_values = np.arange(0, t_total, dt)

    # Calculate positions over time
    x_values = vx0 * t_values
    y_values = vy0 * t_values - 0.5 * g * t_values**2

    return t_values, x_values, y_values

def plot_trajectory(t, x, y):
    plt.plot(x, y)
    plt.title('Projectile Motion')
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Vertical Distance (m)')
    plt.grid(True)
    plt.show()

# Example usage:
v0 = 20  # initial velocity in m/s
theta = 45  # launch angle in degrees

t, x, y = projectile_motion(v0, theta)
plot_trajectory(t, x, y)

import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.81
m = 1.0
l = 1.0

# Initial conditions (small angles)
omega1_0 = 0.0
omega2_0 = 0.0
theta1_0 = 0.1
theta2_0 = 0.1

# Time step and total time
dt = 0.01
T = 20
N = int(T / dt)
time_arr = np.linspace(0, T, N)

# Arrays
theta1_num = np.zeros(N)
theta2_num = np.zeros(N)

# Initialize variables
theta1 = theta1_0
theta2 = theta2_0
omega1 = omega1_0
omega2 = omega2_0

# Euler-Cromer
for i in range(N):
    theta1_num[i] = theta1
    theta2_num[i] = theta2

    a1 = -(g / l) * (2 * theta1 - theta2)
    a2 = (g / l) * (2 * theta1 - 2 * theta2)

    omega1 += a1 * dt
    omega2 += a2 * dt

    theta1 += omega1 * dt
    theta2 += omega2 * dt

# Analytical solution (small-angle approximation)
omega1A = np.sqrt((g / l) * (3 + np.sqrt(5)) / 2)
omega2A = np.sqrt((g / l) * (3 - np.sqrt(5)) / 2)

alpha = (1 + np.sqrt(5)) / 2
beta = (1 - np.sqrt(5)) / 2

C1 = (theta1_0 * (1 - beta)) / (alpha - beta)
C2 = theta1_0 - C1

theta1_A_arr = C1 * np.cos(omega1A * time_arr) + C2 * np.cos(omega2A * time_arr)
theta2_A_arr = alpha * C1 * np.cos(omega1A * time_arr) + beta * C2 * np.cos(omega2A * time_arr)

plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(time_arr, theta1_num, 'g-', label='Numerical')
plt.plot(time_arr, theta1_A_arr, 'm--', label='Analytical')
plt.xlabel('Time (s)')
plt.ylabel(r'$\theta_1$ (rad)')
plt.title('Comparison for angle 1')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time_arr, theta2_num, 'g-', label='Numerical')
plt.plot(time_arr, theta2_A_arr, 'm--', label='Analytical')
plt.xlabel('Time (s)')
plt.ylabel(r'$\theta_2$ (rad)')
plt.title('Comparison for angle 2')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

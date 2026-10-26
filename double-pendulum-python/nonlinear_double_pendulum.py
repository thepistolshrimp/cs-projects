import numpy as np
import matplotlib.pyplot as plt

g = 9.81
m1 = 1.0
m2 = 1.0
l1 = 1.0
l2 = 1.0


def M(q):
    theta1, theta2 = q
    M11 = (m1 + m2) * l1**2
    M12 = m2 * l1 * l2 * np.cos(theta1 - theta2)
    M21 = M12
    M22 = m2 * l2**2
    return np.array([[M11, M12],
                     [M21, M22]])


def b(q, v):
    theta1, theta2 = q
    omega1, omega2 = v

    C_v_1 = -m2 * l1 * l2 * np.sin(theta1 - theta2) * (omega2**2)
    C_v_2 = m2 * l1 * l2 * np.sin(theta1 - theta2) * (omega1**2)

    g_1 = (m1 + m2) * g * l1 * np.sin(theta1)
    g_2 = m2 * g * l2 * np.sin(theta2)

    b1 = C_v_1 - g_1
    b2 = C_v_2 - g_2
    return np.array([b1, b2])


def euler_cromer_step(q, v, dt):
    a = np.linalg.inv(M(q)) @ b(q, v)
    v_new = v + a * dt
    q_new = q + v_new * dt
    return q_new, v_new


def simulate_double_pendulum(q0, v0, t0, t_end, dt):
    nsteps = int((t_end - t0) / dt)
    q_hist = np.zeros((nsteps, 2))
    v_hist = np.zeros((nsteps, 2))
    t_hist = np.linspace(t0, t_end, nsteps)

    q = q0.copy()
    v = v0.copy()

    for i in range(nsteps):
        q_hist[i] = q
        v_hist[i] = v
        q, v = euler_cromer_step(q, v, dt)

    return t_hist, q_hist, v_hist


def positions(q_hist):
    theta1 = q_hist[:, 0]
    theta2 = q_hist[:, 1]

    x1 = l1 * np.sin(theta1)
    y1 = -l1 * np.cos(theta1)

    x2 = x1 + l2 * np.sin(theta2)
    y2 = y1 - l2 * np.cos(theta2)
    return x1, y1, x2, y2


t0 = 0.0
t_end = 20.0
dt = 0.01

q0_1 = np.array([0.1, 0.1])
v0_1 = np.array([0.0, 0.0])

q0_2 = np.array([0.5, 0.2])
v0_2 = np.array([0.0, 0.0])

# Values preserved from the code shown in the submitted report.
q0_3 = np.array([1.0, 0.5])
v0_3 = np.array([0.0, 0.0])

t1, q_H1, _ = simulate_double_pendulum(q0_1, v0_1, t0, t_end, dt)
t2, q_H2, _ = simulate_double_pendulum(q0_2, v0_2, t0, t_end, dt)
t3, q_H3, _ = simulate_double_pendulum(q0_3, v0_3, t0, t_end, dt)

x1_1, y1_1, x2_1, y2_1 = positions(q_H1)
x1_2, y1_2, x2_2, y2_2 = positions(q_H2)
x1_3, y1_3, x2_3, y2_3 = positions(q_H3)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x1_1, y1_1, 'm-', label='Set 1')
plt.plot(x1_2, y1_2, 'b-', label='Set 2')
plt.plot(x1_3, y1_3, 'g-', label='Set 3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectory pendulum 1')
plt.legend()
plt.grid(True)
plt.axis('equal')

plt.subplot(1, 2, 2)
plt.plot(x2_1, y2_1, 'm-', label='Set 1')
plt.plot(x2_2, y2_2, 'b-', label='Set 2')
plt.plot(x2_3, y2_3, 'g-', label='Set 3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectory pendulum 2')
plt.legend()
plt.grid(True)
plt.axis('equal')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t1, q_H1[:, 0], 'm-', label='Set 1: theta1')
plt.plot(t2, q_H2[:, 0], 'b-', label='Set 2: theta1')
plt.plot(t3, q_H3[:, 0], 'g-', label='Set 3: theta1')
plt.xlabel('Time (s)')
plt.ylabel(r'$\theta_1$')
plt.legend()
plt.grid(True)
plt.show()

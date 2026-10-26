import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *


class SEIRO:
    def __init__(self, beta=0.33, r_ia=0.1,
                 r_e2=1.25, lmbda_1=0.33,
                 lmbda_2=0.5, p_a=0.4, mu=0.2):

        self.beta = beta
        self.r_ia = r_ia
        self.r_e2 = r_e2
        self.lmbda_1 = lmbda_1
        self.lmbda_2 = lmbda_2
        self.p_a = p_a
        self.mu = mu

    def __call__(self, t, u):
        beta = self.beta
        r_ia = self.r_ia
        r_e2 = self.r_e2
        lmbda_1 = self.lmbda_1
        lmbda_2 = self.lmbda_2
        p_a = self.p_a
        mu = self.mu

        S, E1, E2, I, Ia, R = u
        N = sum(u)
        dS = -beta * S * I / N - r_ia * beta * S * Ia / N \
            - r_e2 * beta * S * E2 / N
        dE1 = beta * S * I / N + r_ia * beta * S * Ia / N \
            + r_e2 * beta * S * E2 / N - lmbda_1 * E1
        dE2 = lmbda_1 * (1 - p_a) * E1 - lmbda_2 * E2 
        dI = lmbda_2 * E2 - mu * I
        dIa = lmbda_1 * p_a * E1 - mu * Ia
        dR = mu * (I + Ia)
        return [dS, dE1, dE2, dI, dIa, dR]


S_0 = 5.5e6
E1_0 = 0.0
E2_0 = 100.0
I_0 = 0.0
Ia_0 = 0.0
R_0 = 0.0
U0 = [S_0, E1_0, E2_0, I_0, Ia_0, R_0]


model = SEIRO()
solver = RungeKutta4(model)
solver.set_initial_condition(U0)

t_span = (0, 300)
N = 200
t, u = solver.solve(t_span, N)
S = u[:, 0]
E1 = u[:, 1]
E2 = u[:, 2]
I = u[:, 3]
Ia = u[:, 4]
R = u[:, 5]
    


print(max(I))
plt.plot(t, S, label='S')
plt.plot(t, I, label='I')
plt.plot(t, Ia, label='Ia')
plt.plot(t, R, label='R')
plt.legend()
plt.title('Disease dynamics predicted by the SEEIIR model')
plt.xlabel('Time (days)')
plt.ylabel('People in each category')
plt.savefig('seir_fig0.pdf')
plt.show()


#oppgave 1a
def test_SEIRO():
    model = SEIRO()              #Lager en instans av klassen
    u = [1,1,1,1,1,1]
    
    dS = -0.33 * 1 * 1 / 6 - 0.1 * 0.33 * 1 * 1 / 6 - 1.25 * 0.33 * 1 * 1 / 6
    dE1 = 0.33 * 1 * 1 / 6 + 0.1 * 0.33 * 1 * 1 / 6 + 1.25 * 0.33 * 1 * 1 / 6 - 0.33 * 1
    dE2 = 0.33 * (1 - 0.4) * 1 - 0.5 * 1
    dI = 0.5 * 1 - 0.2 * 1
    dIa = 0.33 * 0.4 * 1 - 0.2 * 1
    dR = 0.2 * (1 + 1)

    tol = 1e-10

    computed = np.array(model(0, u))                    #kaller på instansen. __call__ metoden
    expected = np.array([dS, dE1, dE2, dI, dIa, dR])

    abs = np.allclose(computed, expected, tol)
    msg = f"computed != expected"

    assert abs, msg
    return print("test_SEIRO passed")


"""
Substituert u = 1 i likningene(dS, dE1, ...). Brukt np.allclose for å 
sjekke differansen mellom hvert ledd i arrayene expected og computed.  
"""


#oppgave 1b
def solve_SEIR(model, T, N, S_0, E2_0):
    E1_0 = 0.0
    I_0 = 0.0
    Ia_0 = 0.0
    R_0 = 0.0
    U0 = [S_0, E1_0, E2_0, I_0, Ia_0, R_0]

    solver = RungeKutta4(model)
    solver.set_initial_condition(U0)
    t_span = (0, T)
    t, u = solver.solve(t_span, N)
    
    return t, u 

"""
Setter opp intialconditions og anvender Rungekutta4 som ODE-løser. Løser for tiden t_span med antall steps N.
"""



#oppgave 1c
def plot_SEIR(t, u):
    plt.figure()
    S = u[:, 0]
    E1 = u[:, 1]
    E2 = u[:, 2]
    I = u[:, 3]
    Ia = u[:, 4]
    R = u[:, 5]
    plt.plot(t, S, label='S')
    plt.plot(t, I, label='I')
    plt.plot(t, Ia, label='Ia')
    plt.plot(t, R, label='R')
    plt.legend()
    plt.title('Disease dynamics predicted by the SEIRO model')
    plt.xlabel('Time (days)')
    plt.ylabel('People in each category')
    plt.savefig('seir_fig2.pdf')
    plt.show()


model1 = SEIRO(beta=0.4)
t, u = solve_SEIR(model1, 200, 400, S_0, E2_0)
plot1 = plot_SEIR(t, u)

if __name__ == "__main__":
    model1 = SEIRO(beta=0.4)
    t, u  = solve_SEIR(model1, 200, 400, S_0, E2_0)
    plot1 = plot_SEIR(t, u)



"""
Run:
(base) Amers-MacBook-Pro:prosjekt zivor$ python SEIRO.py
142116.11251213297
test_SEIRO passed

"""
























    


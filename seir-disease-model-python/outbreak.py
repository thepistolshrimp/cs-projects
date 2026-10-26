import numpy as np
import matplotlib.pyplot as plt
from SEIR import SEIR, solve_SEIR, plot_SEIR

#Problem 3

def beta(t):
    if t <= 100:
       return 0.4
    elif t >= 100:
       return 0.083

model = SEIR(beta)
t, u = solve_SEIR(model, T = 200, N = 400, S_0 = 5.5e6, E2_0 = 100)
plot_SEIR(t, u)


"""
(base) Amers-MacBook-Pro:prosjekt zivor$ python outbreak.py
198632.38093353316
"""










         
   


      


   















      



















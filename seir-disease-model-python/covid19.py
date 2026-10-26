import numpy as np
import matplotlib.pyplot as plt
from SEIR import SEIR, solve_SEIR, plot_SEIR
from lockdown import Beta

#Problem 5
class SEIRimport(SEIR):
    def __init__(self, beta, sigma, *args, **kwargs):
        self.sigma = sigma

        super().__init__(beta, *args, **kwargs)
        
    

    def __call__(self, t, u):
        dudt = super().__call__(t, u)

        dudt[2] += self.sigma

        return dudt

if __name__ == "__main__":
    beta = Beta('beta_values.txt')
    model = SEIRimport(beta, 10)
    t, u = solve_SEIR(model, T=1000, N = 1000,
                      S_0=5.5e6, E2_0=100)
    plot_SEIR(t, u, components = ['I','Ia'])


"""
(base) Amers-MacBook-Pro:prosjekt zivor$ python covid19.py
8640.33910085535
"""








    

    
    
    

    










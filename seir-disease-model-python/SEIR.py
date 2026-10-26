import numpy as np
import matplotlib.pyplot as plt
from SEIRO import SEIRO, solve_SEIR, plot_SEIR

class SEIR(SEIRO):
    def __init__(self, beta, *args, **kwargs):
        if isinstance(beta, (float, int)):
            self.beta_function = lambda t: beta
        elif callable(beta):
            self.beta_function = beta
        else:
            raise ValueError("beta must be float or callable")
        
        super().__init__(self.beta_function, *args, **kwargs)
    
    def __call__(self, t, u):
        self.beta = self.beta_function(t)
        return super().__call__(t, u)
    

#oppgave b) testing av klassenSEIR  
    
def test_SEIR_beta_const():
     model = SEIR(beta=0.33)
     u = [1,1,1,1,1,1]

     self = model(0, u)
     beta_0 = model.beta

     assert np.isclose(beta_0, 0.33), f"expected {0.33}, got {beta_0}"
     return print("test_SEIR_beta_const passed")







def test_SEIR_beta_var():
    def beta_lin(t):
        return 0.1*t
    
    model = SEIR(beta_lin)
    u = [1,1,1,1,1,1]

    self_0= model(0, u)
    beta_0 = model.beta

    self_4 = model(4, u)
    beta_4 = model.beta

    assert np.isclose(beta_0, 0.0), f"expected {0.0}, got {beta_0}"
    assert np.isclose(beta_4, 0.4), f"expected {0.4}, got {beta_4}"
    return print("test_SEIR_beta_var passed")




#oppgave c) 

def plot_SEIR(t, u, components = ['S', 'I', 'Ia', 'R']):
    plt.figure()
    
    components_index = {'S': 0, 'E1': 1, 'E2': 2, 'I': 3, 'Ia': 4, 'R': 5}

    for c in components:
        dx = components_index[c]
        plt.plot(t, u[:, dx], label = c)    
    
    I = u[:,3]
    print(max(I))            #max functionvalue of I
    
    plt.legend()
    plt.title('Disease dynamics predicted by the SEIR model')
    plt.xlabel('Time (days)')
    plt.ylabel('People in each category')
    plt.savefig('seir_fig3.pdf')
    plt.show()
    


if __name__ == "__main__":
    test_SEIR_beta_const()
    test_SEIR_beta_var()
    model = SEIR(beta = 0.4)
    t, u = solve_SEIR(model, T = 200, N = 400, S_0 = 5.5e6, E2_0 = 100)
    plot_SEIR(t,u)

"""
Maximum infected people during this time period is equal to 258543
51709 people need hospital care
2585 people need ventilators
So this basically means that 1885 people will not get ventilators, they are more likely to die

Run:
(base) Amers-MacBook-Pro:prosjekt zivor$ python SEIR.py
test_SEIR_beta_const passed
test_SEIR_beta_var passed
258543.46967265086
"""




















    

    









    













    


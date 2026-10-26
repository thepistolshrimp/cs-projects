import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta


#Problem 4
class Beta:
   def __init__(self, filename):
      self.days = []
      self.values = []

      self.t0 = date(2020, 2, 15)

      with open(filename) as infile:
         infile.readline()
         infile.readline()
         for line in infile:
            line = line.split()
            d = line[0].strip()
            v = float(line[2].strip())

         
            curr_date = self.str2date(d)
            n_days = self.tdelta(curr_date)

            self.days.append(n_days)
            self.values.append(v)
   
   def str2date(self, d):
      day, month, year = (int(n) for n in d.split('.'))
      return date(year,month,day)
   
   def tdelta(self, curr_date):
      return (curr_date - self.t0).days

   
   def __call__(self, t):
      if t <= self.days[0]:
         return self.values[0]
      for i in range(len(self.days)-1):
         if self.days[i] <= t < self.days[i+1]:
            return self.values[i]
         elif t >= self.days[-1]:
            return self.values[-1]
   
   def vectorized(self):
      return np.vectorize(self.__call__)    #vektoriserer __call__ metoden
   
   def plot(self, T):
      t = np.linspace(0, T, 1000)
      v_beta = self.vectorized()
      beta = v_beta(t)
      print(t)
      print(beta)
      plt.plot(t, beta)
      plt.xlabel('Time (days)')
      plt.ylabel('\u03B2')
      plt.savefig('beta_fig4')
      plt.show()
   

if __name__ == "__main__":
    from SEIR import SEIR, solve_SEIR, plot_SEIR
    beta = Beta('beta_values.txt')
    beta.plot(1000)
    model = SEIR(beta)
    t, u = solve_SEIR(model, T=1000, N = 1000,
                      S_0=5.5e6, E2_0=100)
    plot_SEIR(t, u, components = ['I','Ia'])

"""
Model is not taking into account the flux of imported people coming in, which most likely will increase beta values
and causing new waves. The number of infected is too low to cause a new wave, we see that the number drops to almost zero
and stays approximately constant, because it does not account for the import of I.



Har brukt chatGPT til noe hjelp med syntaks og feilsøking.
"""

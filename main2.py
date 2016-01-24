"""
Computes equilibrium price and quantities, take 2.
"""
from numpy import exp
from scipy.optimize import bisect

def supply(price, b):
   return exp(b * price) - 1

def demand(price, a, epsilon):
   return a * price**(-epsilon)

def compute_equilibrium(a, b, epsilon):
    plow = 0.1
    phigh = 10.0
    def excess_supply(price):
        return supply(p, b) - demand(p, a, epsilon)

    pclear = bisect(excess_supply, plow, phigh)
    return pclear

parameter_list = ((1, 0.1, 1),
                  (2, 0.1, 1),
                  (1, 0.2, 1),
                  (1, 0.1, 2))

for parameters in parameter_list:
    print("Price = {}".format(compute_equilibrium(*parameters)))

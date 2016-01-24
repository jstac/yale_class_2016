"""
Computes equilibrium price and quantities.
"""
from numpy import exp

## Parameters
a = 1
b = 0.1
epsilon = 1

def supply(price):
   return exp(b*price) - 1

def demand(price):
   return a*(price**(-epsilon))

mxiter = 30
toler = 1.0e-6

plow = 0.1
phigh = 10.0

niter = mxiter

for i in range(mxiter):

    pcur = (plow + phigh)/2
    yd = demand(pcur)
    ys = supply(pcur)
    excesssupply = ys - yd

    if excesssupply > 0:
        phigh = pcur
    else:
        plow = pcur

    diff = abs(phigh - plow)

    if diff <= toler:
        niter = i
        break

pclear = (plow + phigh)/2
yd = demand(pcur)
ys = supply(pcur)
excesssupply = ys - yd

print(niter, pclear, yd, ys, excesssupply)

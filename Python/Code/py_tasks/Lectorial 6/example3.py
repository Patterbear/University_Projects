import random as rd
def mysqrt(x, eps):
    """Inputs: two numbers x, eps such that x >= 0, eps>=0
    Output: a number res such that x-eps <= res*res <=x+eps """
    g = rd.uniform(0, x) #random guess
    gsquared = g*g
    while (gsquared<x-eps or gsquared>x+eps):
        g = (g+x/g)/2 #new g is average of g and x/g
        gsquared = g*g
    return g

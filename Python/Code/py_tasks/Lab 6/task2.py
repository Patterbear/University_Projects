import random as rd

def mysqrt(x, eps):
 #Inputs:two numbers x, eps such that x >= 0, eps>=0
 #Output: a number res such that x-eps <= res*res <=x+eps
    file = open("g_values.txt", "a")
    i = 1
    g = rd.uniform(0, x) #random guess
    gsquared = g*g
    try:
        assert g > 0
        while (gsquared<x-eps or gsquared>x+eps):
             g = (g+x/g)/2 #new g is average of g and x/g
             gsquared = g*g
             file.write("At iteration " + str(i) + " , the estimated squared root is " + "{:.3f}".format(g) + "\n")
             i +=1
        return g
    except ZeroDivisionError:
        print("x cannot be divided by 0")
        
    except AssertionError:
        print("Inputs are invalid")



print(mysqrt(45, 1.e-8))

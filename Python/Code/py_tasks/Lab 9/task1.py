from math import gcd

class Fraction(object):
    def __init__(self, num, denom):
        g = gcd(num, denom)
        num = int(num/g)
        denom = int(denom/g)
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def to_float(self):
        return self.num / self.denom

    def __add__(self, other):
        n = (self.num*other.denom)+(other.num*self.denom)
        d = self.denom*other.denom
        return Fraction(n, d)

    def __sub__(self, other):
        n = (self.num*other.denom)-(other.num*self.denom)
        d = self.denom*other.denom
        return Fraction(n, d)

    def __mul__(self, other):
        n = self.num*other.num
        d = self.denom*other.denom
        return Fraction(n, d)

    def __truediv__(self, other):
        n = self.num*other.denom
        d = self.denom*other.num
        return Fraction(n, d)
        
    def __eq__(self, other):
        return self.num==other.num and self.denom==other.denom

    def scale(fraction_list, factor):
        scaled = []
        for i in range(len(fraction_list)):
            scaled.append(str(fraction_list[i] / Fraction(int(factor), 1)))
        return scaled

    def printListOfFractions(fraction_list):
        f_list = []
        for i in range(len(fraction_list)):
            f_list.append(str(fraction_list[i]))
        print (f_list)   




f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
f3 = Fraction(2, 4)
f4 = Fraction(1, 4)
f = f1+f2

f_list = [f1, f2, f3, f4]

print(Fraction.scale(f_list, 10))
Fraction.printListOfFractions(f_list)

##print(f3 - f4)
##print(f3)
##print(f1==f2)
##print(f.to_float())
##print(f1 * f4)
##print(f1 / f4)


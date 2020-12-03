from math import gcd, nan

class Fraction(object):
    def __init__(self, num, denom):    
        try:
            assert denom != 0
            g = gcd(num, denom)
            num = int(num/g)
            denom = int(denom/g)
           
            self.num = num
            self.denom = denom
            
        except AssertionError:
            print("Fraction denominator cannot be zero! (Division by 0 is impossible)")
            return None
       
        except TypeError:
            print("Inputs are not integer values! (Must be integers)")
            return None
        

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
            try:
                scaled.append(str(fraction_list[i] / Fraction(int(factor), 1)))
            except ZeroDivisionError:
                scaled.append(nan)
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
f6 = Fraction(1, 0)
f5 = Fraction("string", "hello")

f_list = [f1, f2, f3, f4]

print(Fraction.scale(f_list, 10))
Fraction.printListOfFractions(f_list)

##print(f3 - f4)
##print(f3)
##print(f1==f2)
##print(f.to_float())
##print(f1 * f4)
##print(f1 / f4)


class Fraction(object):
    def __init__(self, num, denom):
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

    def __eq__(self, other):
        return self.num==other.num and self.denom==other.denom


f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
f = f1+f2

print(f)
print(f1==f2)
print(f.to_float())

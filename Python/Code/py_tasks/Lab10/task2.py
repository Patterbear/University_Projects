from math import pi

class Point(object):
    """ Point class for representing and manipulating x,y coordinates. """
    # for the constructor
    def __init__(this, x, y):
        """ Create a new point at a given coordinates """
        this.x = x
        this.y = y
    # defining own print method
    def __str__(this):
        return "("+str(this.x)+","+str(this.y)+")"


class Circle(Point):
    def __init__(self, x, y, r):
        Point.__init__(self, x, y)
        self.radius = r

    def __str__(self):
        return "Location = "+Point.__str__(self)+"; Radius = "+str(self.radius)

class Cylinder_i(Circle):
    def __init__(self, x, y, r, l):
        Point.__init__(self, x, y)
        Circle.__init__(self, x, y, r)
        self.length = l
    def __str__(self):
        return "Location = "+Point.__str__(self)+"; Radius = "+str(self.radius)+"; Length: "+str(self.length)

class Cylinder_c(object):
    def __init__(self, c, l):
        self.centre = Point.__str__(c)
        self.radius = c.radius
        self.length = l

    def __str__(self):
        return "Location = "+self.centre+"; Radius = "+str(self.radius)+"; Length: "+str(self.length)

p = Point(1, 2)
circ = Circle(1, 2, 5)
c = Cylinder_i(1, 2, 5, 10)
c2 = Cylinder_c(circ, 10)

print(c)
print(c2)


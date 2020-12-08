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


class Square(Point):
    def __init__(self, x=0, y=0, side=1):
        Point.__init__(self, x, y)
        self.side = side
        
    def __str__(self):
        return "Location: " + Point.__str__(self) + " Side: " + str(self.side)
    
    def set_side(self, side):
        self.side = side
        
    def get_side(self):
        return self.side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4*self.side


class Square2:
    def __init__(self, p=Point(0,0), side=1):
        self.centre = p
        self.side = side
        

    
p = Point(2, 4)
print(Square())
square1 = Square(p, 0, 4)

print(square1)
print(square1.get_side())
print(square1.area())
print(square1.perimeter())



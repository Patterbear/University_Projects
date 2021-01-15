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



class Segment(object):
    def __init__(self, point, angle=90, radius=10):
        self.centre = point
        self.angle = angle
        self.radius = radius
        self.circumference = 2*pi*self.radius

    def __str__(self):
        return "Centre: " + str(self.centre) + ", Angle: " + str(self.angle) + " degrees, Radius: " + str(self.radius)

    def distance(self):
        return 2*pi*self.radius * (self.angle / 360)

p = Point(1, 2)
s = Segment(p, 180, 5)

print(s.distance())

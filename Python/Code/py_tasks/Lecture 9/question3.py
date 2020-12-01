class Car:
    def __init__(self, num_doors=3, colour="red"):
        self.num_doors = num_doors
        self.colour = colour

    def get_num_doors(self):
        return self.num_doors

    def get_colour(self):
        return self.colour

    def set_num_doors(g_num_doors):
        self.num_doors = g_num_doors

    def set_colour(g_colour):
        self.colour = g_colour


micra = Car(5, "yellow")
leaf = Car()

print(micra.get_num_doors())
print(leaf.get_num_doors())
        

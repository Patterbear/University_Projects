from math import floor
from random import randint, random

class City:
    def __init__(self, name, population, rog, possible_casulties):
        self.name = name
        self.population = population
        self.rog = rog
        self.possible_casulties = possible_casulties

    def __str__(self):
        return"Name: " + self.name + "\n" "Population: " + str(self.population) + "\n" + "Growth Rate: " + str(self.rog) + "%\n" + "Possible Casulties: " + str(self.possible_casulties)

    def advance_year(self, other, years):
        for i in range(self.population):
            if random() > 0.5:
                if randint(0, self.population+other.population)  < self.population:
                    self.population = self.population - 1
        for i in range(years):
            self.population = floor(self.population * (1.0 + self.rog*0.01))
        disasters = []
        for i in range(years):
            if randint(0, 9) == 1:
                disasters.append(True)
            else:
                disasters.append(False)
        for i in range(len(disasters)):
            if disasters[i]:
                self.population = self.population - self.possible_casulties



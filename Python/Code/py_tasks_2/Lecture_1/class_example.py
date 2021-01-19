class Person(object):

    def __init__(self):
       self.Name = ""
       self.Age = 30

    def __init__(self, name, age):
        self.Name=name
        self.Age=age

    def getName(self):
        return self.Name

    def setName(self, name):
        self.Name=name

    def getAge(self):
        return self.Age

    def setAge(self, age):
        self.Age=age

    def __str__(self):
        return "Name: " + str(self.Name) + "\n Age: " + str(self.Age)


p1=Person("Benjamin", 18)
print(p1.getName())
print(p1)

    

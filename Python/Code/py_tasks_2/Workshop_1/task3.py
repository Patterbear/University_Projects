class Student(object):

    def __init__(self, name, id_num, age=0, mark=0):
        self.name = name
        self.id_num = id_num
        self.age = age
        self.mark = mark

    def Display(self):
        print("Name: " + self.name + ", ID Number: " + self.id_num + ", Age: " + str(self.age) + ", Mark: " + str(self.mark))


    def setAge(self, age):
        self.age = age

    def setMarks(self, mark):
        self.mark = mark



s1 = Student("Benjamin", "BWTFM1")
s1.Display()
s1.setAge(18)
s1.setMarks(100)
s1.Display()

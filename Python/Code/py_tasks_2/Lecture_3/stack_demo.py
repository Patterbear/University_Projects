class Stack(object):

    def __init__(self, aList):
        self.size = len(aList)
        self.stack = aList


    def __str__(self):
        stack_str = "Bottom ->  | "
        for i in range(len(self.stack)):
            #print(i)
            stack_str += str(self.stack[i]) + " | "
        stack_str += "  <- Top"

        return stack_str

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            self.stack.pop()

    def pop(self, num):
        if num == "all":
            self.stack = []
        elif  num > len(self.stack):
            print("Number exceeds stack size")
        else:
            for i in range(num):
                self.stack.pop()

    def push(self, val):
        if len(self.stack) == self.size:
            print("Stack is full.")
        else:
            self.stack.append(val)

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size


#Test Script

def test_script():
    stack = Stack([1,2,3,4,5])
    print(stack)
    stack.pop(6)
    print(stack)
    stack.pop(5)
    stack.push(10)
    stack.push(5)
    stack.push(8)
    print(stack)
    stack.pop("all")
    print(stack)
    stack.push(10)
    stack.push(8)
    stack.push(4)
    stack.push(7)
    print(stack)
    stack.pop("all")
    stack.setSize(3)
    stack.push(10)
    stack.push(5)
    stack.push(6)
    stack.push(10)
    print(stack)

test_script()



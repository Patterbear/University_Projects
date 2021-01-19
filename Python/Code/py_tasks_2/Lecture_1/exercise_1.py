num1 = int(input(""))
num2 = int(input(""))
num3 = int(input(""))

def Sum_Num(num1, num2):
    return(num1+num2)

def Product(n, num3):
    return(n*num3)


print(Product(Sum_Num(num1, num2), num3))

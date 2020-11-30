id = input("")
days = int(input(""))
hours = int(input(""))
pt = input("")

if pt == "y":
    salary = hours * days * 15

else:
    salary = days * 150

print(salary)

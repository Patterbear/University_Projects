import enchant

r = input("Word: ")[: : -1]
d = enchant.Dict("en_GB")

if d.check(r) == True:
    print("Yes")
else:
    print("No")

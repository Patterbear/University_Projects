n = int(input("Number: "))

for i in range(n+1):
    si = str(i)
    while(len(si) < len(str(n)) ):
            si = "0" + si
    print(si)

def getProduct(text):
    t = text.split("*")
    n = []
    for i in range(len(t)):
        if t[i] == '*':
            continue
        else:
            n.append(int(t[i]))
            
    p = n[0]
    for i in range(1, len(n)):
        p = p * n[i]
    return p


print(getProduct("12*2*10"))
print(getProduct("4*2*3*1"))
        

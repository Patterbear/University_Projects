s = list(input("Enter String: "))
c = input("Enter Character to censor: ")[0]

for i in range(len(s)):
    if s[i] == c:
        s[i] = '*'
        
print("".join(s))

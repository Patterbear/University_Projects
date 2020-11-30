string = input("String: ").lower()
char_list = input("List: ").lower().split()

v = 0

for e in string:
    if e in char_list:
        v += 1
    if v >= len(string):
        print("True")
        

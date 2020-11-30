try:
     f = open("data.txt", "r+")
     count = 0
     for line in f:
        count = count + 1
     print('Line Count:', count)
except FileNotFoundError:
     print("File does not exists!")
finally:
     f.close()

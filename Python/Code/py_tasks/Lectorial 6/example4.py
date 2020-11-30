try:
     f = open("data.txt")
     fh = open(f)
     count = 0
     for line in fhand:
        count = count + 1
     print('Line Count:', count)
except FileNotFounderror:
     print("File does not exists!")
finally:
     fh.close()

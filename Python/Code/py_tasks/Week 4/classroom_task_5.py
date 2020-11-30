letter_file = open("letter.txt")
letter = []
for line in letter_file:
    line = line.strip()
    letter.append(line)
letter_file.close()

print(letter)

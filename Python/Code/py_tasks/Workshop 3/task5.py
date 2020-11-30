sum = 0
words = input("Input 10 words: ").upper().split()

for i in range(len(words)):
    if words[i] == 'A' or 'E' or 'I' or 'O' or 'U':
        sum += 1

print(sum)

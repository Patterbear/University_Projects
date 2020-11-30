def letter_counter(word):
    word = word.lower()
    d = {}
    for i in range(len(word)):
        if word[i] in d:
            d[word[i]]+= 1
        else:
            d[word[i]] = 1
    return d

def letter_count(dictionary):
    for i in dictionary:
        print(str(dictionary[i]))


print(letter_counter("Python"))
letter_count(letter_counter("hello"))
        

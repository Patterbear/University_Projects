def letter_counter(word):
    word = word.lower()
    h ={}
    for i in range(len(word)):
        if word[i] in h:
            h[word[i]] += 1
        else:
            h[word[i]] = 1
    
    return h, len(word)


print(letter_counter("hello"))

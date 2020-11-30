def word_count(filename):
    d = {}
    words = open(filename).read().split()
    for i in range(len(words)):
        if words[i] in d:
            d[words[i]] += 1
        else:
            d[words[i]] = 1
    return tuple((d.items()))
            

print(word_count("file.txt"))

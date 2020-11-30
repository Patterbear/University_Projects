files = ["doc1.txt", "doc2.txt", "doc3.txt"]
keywords = ["car", "a", "casinoville"]

def word_search(files, search):
    result = ()
    for i in range(len(files)):
        file = open(files[i]).read().split()
        for j in range(len(file)):
            if file[j].lower() == search.lower():
                result = result + (files[i],)
    return(result)

def multi_word_search(files, keywords):
    result = {}
    for i in range(len(keywords)):
        result[keywords[i]] = ()
        for j in range(len(files)):
            file = open(files[j]).read().split()
            for k in range(len(file)):
                file[k] = file[k].lower()
            if keywords[i] in file:
                result[keywords[i]] += (files[j],)
    return(result)
        

print(word_search(files, "A"))
print(multi_word_search(files, keywords))

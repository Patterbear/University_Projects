file1 = open("doc1.txt").read().split(); file2 = open("doc2.txt").read().split(); file3 = open("doc3.txt").read().split()
files = [file1, file2, file3]

def word_search(files):
    d = {}
    for i in range(len(files)):
        for j in range(len(files[i])):
            files[i][j] = files[i][j].lower()
            if files[i][j] in d:
                d[files[i][j]] += 1
            else:
                d[files[i][j]] = 1
    return d
    


print(word_search(files))

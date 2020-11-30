def anagram(wList,word):
    sortedWord = ' '.join(sorted(word))
    anagramList = []
    wordIndex = 0
    while wordIndex < len(wList):
        tmp = ' '.join(sorted(wList[wordIndex]))
        if tmp == sortedWord:
            anagramList.append(wList[wordIndex])
        wordIndex += 1
    return anagramList

wordList = ['azer', 'zare', 'zara', 'alex', 'Henry', 'Ali', 'Jack']
theWord = 'reza'
print(anagram(wordList, theWord))

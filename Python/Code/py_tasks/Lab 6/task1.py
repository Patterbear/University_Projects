def file_readout(filename):
    #Input: Takes in the name of a file found in the current directory (D:\Programming\Python\Tasks\Lab 6)
    #Output: None, but prints contents of file to screen in capital letters
    for line in open(filename):
        print(line.upper())


file_readout("text.txt")

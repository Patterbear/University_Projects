def read_data(filename):
    file = open(filename, "r+")
    data_array = [line.split() for line in file]
    return data_array

def row_averages(data_array):
    total = 0
    for i in range(len(data_array)):
        for j in range(len(data_array[i])):
            total = total + float(data_array[i][j])
        print (total)


row_averages(read_data("data.txt"))
        

import csv
import numpy

def read_csv_data(filename):
    file = open(filename, newline = '')
    csv_list = list(csv.reader(file))

    return csv_list

def averages(csv_list):
    averages_list = []
    for i in range(len(csv_list)):
        total = 0.0
        for j in range(len(csv_list[i])):
            try:
                total = total + float(csv_list[i][j])
            except ValueError:
                continue
        if total == 0.0:
            total = numpy.nan
        averages_list.append(total / len(csv_list[i]))
        
    return averages_list

def print_averages(averages_list):
    for i in range(len(averages_list)):
        print("Row " + str(i) + " average is " + str("{:.3f}".format(averages_list[i])))

#print(averages(read_csv_data("data.csv")))

#print(read_csv_data("data.csv"))

print_averages(averages(read_csv_data("data.csv")))

table = open("temp.txt", "r+")

temps = table.read().splitlines()
clean_list = []

for i in range(len(temps)):
    temp_list = list(temps[i])
    clean = ""
    for j in range(len(temps[i])):
        if temp_list[j].isalpha() == True or temp_list[j] == ",":
            temp_list[j] = ''
    clean_list.append(clean.join(temp_list))

def min_temp(clean_list):
    min = int(clean_list[0])
    for i in range(len(clean_list)):
        if int(clean_list[i]) < min:
            min = int(clean_list[i])
    return str(min)

def max_temp(clean_list):
    max = int(clean_list[0])
    for i in range(len(clean_list)):
        if int(clean_list[i]) > max:
            max = int(clean_list[i])
    return str(max)

print("The minimum temperature of the week is: " + min_temp(clean_list) + " and the maximum temperature of the week is: " + max_temp(clean_list))

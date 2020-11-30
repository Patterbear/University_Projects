numList1 = [4, -21, 2, -20]
numList2 = [3, -5, 2, -6, -1]

def abs_val(numList):
    closest_to_zero = numList[0]
    print(closest_to_zero)
    for i in range(1, len(numList)):
        if numList[i] > 0 and closest_to_zero > 0 and numList[i] < closest_to_zero:
            print(str(numList[i]) + " is positive and so is the ctz: " + str(closest_to_zero))
            closest_to_zero = numList[i]
            print("New closest: " + str(closest_to_zero))
        elif numList[i] < 0 and closest_to_zero < 0 and numList[i] > closest_to_zero:
            print(str(numList[i]) + " is negative and so is the ctz: " + str(closest_to_zero))
            closest_to_zero = numList[i]
            print("New closest: " + str(closest_to_zero))
        elif numList[i] == 0:
            closest_to_zero = numList[i]
            print("New closest: " + str(closest_to_zero))
        else:
            continue
    print(closest_to_zero)

abs_val(numList1)
abs_val(numList2)

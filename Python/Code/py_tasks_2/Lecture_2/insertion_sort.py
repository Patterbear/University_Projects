def swap(u_list, i, j):
    temp = u_list[i]
    u_list[i] = u_list[j]
    u_list[j] = temp


def shift(u_list, j):
    while u_list[j-1] > u_list[j] and j>0:
        swap(u_list, j-1, j)
        j = j-1


def insertion_sort(u_list):
    n = len(u_list)
    for k in range(1, n):
        shift(u_list, k)
    #return u_list


u_list = [6, 5, 3, 1]
insertion_sort(u_list)
print(u_list)

u_list = [10, -4, -1, 20, 13, -3]


def get_min(u_list, start, stop):
    min_index = start
    for i in range(start+1, stop):
        if u_list[i] < u_list[min_index]:
            min_index = i

    return min_index

def swap(u_list, i, j):
    temp = u_list[i]
    u_list[i] = u_list[j]
    u_list[j] = temp

def ss(u_list):
    n = len(u_list)
    for index in range(n):
        min_pos = get_min(u_list, index, n)

        swap(u_list, index, min_pos)

    return u_list


print(ss(u_list))
        

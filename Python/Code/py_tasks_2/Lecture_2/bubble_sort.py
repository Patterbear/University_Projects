def bubble_sort(u_list):
    n = len(u_list)
    i = 0
    while i < n -1:
        j = 0
        while j < n - 1:
            if u_list[j] > u_list[j+1]:
                swap(u_list, j, j+1)
            j+=1
        i += 1


def swap(u_list, i, j):
    tmp = u_list[i]
    u_list[i] = u_list[j]
    u_list[j] = tmp



u_list = [5, 4, 7, 1, 2]
bubble_sort(u_list)
print(u_list)
            
                       

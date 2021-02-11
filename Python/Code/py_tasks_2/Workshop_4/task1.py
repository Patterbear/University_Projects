def factorial_list(n):
    if n == 1:
        return [1]

    fac_list = factorial_list(n-1)
    new_val = fac_list[-1] * n
    fac_list.append(new_val)
    return fac_list


print(factorial_list(5))

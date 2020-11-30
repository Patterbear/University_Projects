def change_place(racers):
    racers[0], racers[-1] = racers[-1], racers[0]
    return racers


print(change_place(['Ben', 'Hello', 'Bye']))


def swap_nums(x, y):
    x = x+y
    y = x - y
    x = x - y

    return(x, y)

print(swap_nums(-5, 10))

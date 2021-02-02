stack = [9, 2, 40, 10, 3, 2, 4, 30]

def find_largest(stack):
    biggest = []
    biggest.append(stack[-1])
    stack.pop()
    for i in range(len(stack)):
        if stack[-1] > biggest[-1]:
            biggest.append(stack[-1])
            stack.pop()
        else:
            stack.pop()
        
    return biggest[-1]


print(find_largest(stack))
    

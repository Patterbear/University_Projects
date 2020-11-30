def  contains_happy_number(nums):

    """ Inputs: a set of integers

        Outputs: True/False if the given set of numbers is happy. A happy set contains at least one number divisible by 7. """

    for num in nums:

        if num % 7 == 0:

            return True

    return False

print(contains_happy_number({1, 2, 3, 7, 10, 21}))
print(contains_happy_number({7, 2, 3, 1, 10, 21}))
print(contains_happy_number({1, 2, 3, 5, 10, 20}))

from functools import reduce


def square_of_sum(number):
    # generate list of numbers
    nums = list(range(1, number + 1))
    # return a reduced total from list of numbers and square it
    return pow(reduce(lambda x, y: x + y, nums), 2)


def sum_of_squares(number):
    # generate list of numbers
    nums = list(range(1, number + 1))
    # generate mapped list of squares from numbers
    squared_nums = list(map(lambda n: pow(n, 2), nums))
    # return the sum of the squared numbers
    return reduce(lambda x, y: x + y, squared_nums)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)

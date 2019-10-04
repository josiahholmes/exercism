from string import ascii_uppercase
from functools import reduce


def adder(x, y):
    return x + y


def is_valid(isbn):
    # create a reversed list of numbers 1-10: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ten = list(reversed(range(1, 11)))
    # replace all '-' in isbn arguments to get clean string
    isbn = isbn.replace('-', '')
    # create a list of all uppercase alphabet characters excluding X
    invalid_chars = list(ascii_uppercase.replace('X', ''))

    try:
        # check if ISBN string length is 10 and no invalid characters are in it
        if len(isbn) == 10 and all(char not in isbn for char in invalid_chars):
            # convert string numbers to int
            # check if ISBN ends with X and replace with 10
            if isbn.endswith('X'):
                isbn = [int(num) if (num.isdigit())
                        else 10 for num in isbn]
            # if ISBN doesn't end with X,
            # only create a list of numbers if string numbers are digits
            else:
                isbn = [int(num) for num in isbn if num.isdigit()]
            # create a list of multiples combining both isbn and ten list
            # using lambda and map functions
            multiples = list(map(lambda x, y: x * y, isbn, ten))
            # reduce multiples list to a total sum and mod 11
            return (reduce(adder, multiples) % 11 == 0)
        else:
            return False
    except Exception as ex:
        raise Exception("Error: Cannot validate ISBN - {0}".format(ex))

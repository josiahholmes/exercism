from functools import reduce


def classify(number):
    try:
        if number == 1:
            aliquot_sum = 0
        else:
            # create a factors list
            factors = [f for f in range(1, number) if number % f == 0]
            # reduce factors list to aliquot sum
            aliquot_sum = reduce(lambda x, y: x + y, factors)

        # classify number by aliquot sum comparison
        return "perfect" if aliquot_sum == number else "abundant" if aliquot_sum > number else "deficient"
    except Exception as ex:
        raise ValueError(
            f'Error in calculating aliquot sum: {ex}.')

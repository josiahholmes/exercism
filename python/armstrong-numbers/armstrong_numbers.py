def is_armstrong_number(number):
    num_len = len(str(number))
    total = sum([pow(int(num), num_len) for num in str(number)])
    return number == total

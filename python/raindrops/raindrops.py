def convert(number):
    factors = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }
    return ''.join(value for key, value in factors.items()
                    if number % key == 0) or str(number)

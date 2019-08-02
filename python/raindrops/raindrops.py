def convert(number):
    factors = {
        '3': 'Pling',
        '5': 'Plang',
        '7': 'Plong'
    }
    raindrop_speak = ''.join([factors[str(idx)] for idx in range(1, number+1)
                              if ((number % idx == 0) and (str(idx) in factors))])
    return raindrop_speak if raindrop_speak else str(number)

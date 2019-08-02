def distance(strand_a, strand_b):
    if (len(strand_a) != len(strand_b)):
        raise ValueError('Strands are not of equal length.')
    return len([letter for letter in zip(strand_a, strand_b) if letter[0] != letter[1]])

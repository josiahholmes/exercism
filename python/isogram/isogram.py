def is_isogram(string):
    # clean string
    string = list(string.replace('-', '').replace(' ', '').lower())
    return sorted(string) == sorted(set(string))

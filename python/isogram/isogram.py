def is_isogram(string):
    # clean string
    string = [char.lower() for char in string if char.isalpha()]
    return sorted(string) == sorted(set(string))

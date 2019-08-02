def is_pangram(sentence):
    alphabet = {}
    for char in sentence.lower():
        if (97 <= ord(char) <= 122):
            if char not in alphabet:
                alphabet[char] = 'Found!'
    return len(alphabet) == 26

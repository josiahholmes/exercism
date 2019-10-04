def find_anagrams(word, candidates):
    return [candidate for candidate in candidates if (candidate.lower() != word.lower()) and
            (''.join(sorted(candidate.lower())) == ''.join(sorted(word.lower())))]

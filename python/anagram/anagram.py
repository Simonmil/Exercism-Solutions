def find_anagrams(word, candidates):
    word = word.lower()
    anagrams = []
    for candidate in candidates:
        candidate = candidate.lower()
        if all(letter in word for letter in candidate) and word != candidate:
            anagrams.append(candidate)

    return anagrams

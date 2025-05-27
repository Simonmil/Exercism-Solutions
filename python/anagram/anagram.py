def find_anagrams(word, candidates):
    word = word.lower()
    anagrams = []
    for candidate in candidates:
        #candidate = candidate.lower()
        if all(letter.lower() in word for letter in candidate) and word != candidate.lower() and len(word) == len(candidate):
            anagrams.append(candidate)
    print(anagrams)
    return anagrams

def find_anagrams(word, candidates):
    word = word.lower()
    anagrams = []
    for candidate in candidates:
        #candidate = candidate.lower()
        if all(candidate.lower().count(letter) == word.count(letter) for letter in word) and word != candidate.lower() and len(word) == len(candidate):
            anagrams.append(candidate)
    print(anagrams)
    return anagrams

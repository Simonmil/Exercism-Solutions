def is_pangram(sentence):
    sentence = sentence.replace(' ','').lower()
    letters = []
    for index,letter in enumerate(sentence):
        if not letter in letters and letter.isalpha():
            letters.append(letter)
            if len(letters) == 26:
                return True
    return False

    """
    import string
    return all(character in sentence.lower() for character in string.ascii_lowercase)
    """
def is_isogram(string):
    string = string.replace(" ","").lower()
    return all(string.count(character) == 1 and character.isalpha() or not character.isalpha() for character in string)

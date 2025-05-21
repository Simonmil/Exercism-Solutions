import string

"""
I was helped by AI Agent
"""

def rotate(text, key):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    code = []
    if key == 26: key = 0

    for letter in text:
        match letter:
            case l if l in lower:
                idx = lower.index(l)
                code.append(lower[(idx + key) % 26])
            case l if l in upper:
                idx = upper.index(l)
                code.append(upper[(idx + key) % 26])
            case _:
                code.append(letter)

    return ''.join(code)
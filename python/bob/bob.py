def response(hey_bob):
    if "?" in hey_bob:
        return "Sure."
    elif hey_bob == hey_bob.upper():
        return "Whoa, chill out!"
    elif hey_bob == hey_bob.upper() and "?" in hey_bob:
        return "Calm down, I know what I'm doing!"
    elif len(hey_bob) == 0:
        return "Fine. Be that way!"
    else:
        return "Whatever."
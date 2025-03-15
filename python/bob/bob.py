def response(hey_bob):
    if len(hey_bob) == 0:
        return "Fine. Be that way!"
    elif  hey_bob == hey_bob.upper() and "?" in hey_bob:
        return "Calm down, I know what I'm doing!"
    elif hey_bob == hey_bob.upper():
        return "Whoa, chill out!"
    elif hey_bob[-1] == "?":
        return "Sure."
    else:
        return "Whatever."
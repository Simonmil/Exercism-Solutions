def response(hey_bob):
    hey_bob = hey_bob.strip()
    #return "foobar"
    if len(hey_bob) == 0:
        return "Fine. Be that way!"
    elif hey_bob == hey_bob.upper() and hey_bob.lower() != hey_bob.upper():
        if hey_bob[-1] == "?":
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif hey_bob[-1] == "?":
        return "Sure."
    else:
        return "Whatever."
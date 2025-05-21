def is_valid(isbn):
    isbn = isbn.replace("-","")
    if not len(isbn) == 10 or not isbn[:9].isnumeric() or not isbn.isnumeric() and not isbn[-1] == 'X':
        return False

    sum = 0
    for index,number in enumerate(range(10,0,-1)):
        if isbn[index] == 'X':
            sum += 10 * number
        else:
            sum += int(isbn[index]) * number
    
    return sum % 11 == 0

def square(number):
    if not 0 < number < 65:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

def total():
    sum = 0
    for number in range(1,65):
        sum += square(number)
    return sum

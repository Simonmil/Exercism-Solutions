def is_armstrong_number(number):
    sum = 0
    number_as_string = str(number)
    for digit in number_as_string:
        sum += int(digit) ** len(number_as_string)
    return sum == number

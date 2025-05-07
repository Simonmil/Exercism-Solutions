def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1: 
        raise ValueError("Classification is only possible for positive integers.")
    
    denum = 1
    factor_sum = 0
    while denum < number:
        if number % denum == 0:
            factor_sum += denum
        denum += 1

    if factor_sum == number:
        return 'perfect'
    elif factor_sum < number:
        return 'deficient'
    return 'abundant'
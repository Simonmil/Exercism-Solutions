def is_triangle(sides):
    a, b, c = sides
    return a + b >= c and b + c >= a and c + a >= b and all(sides)

def equilateral(sides):
    return len(set(sides)) == 1 and is_triangle(sides)

def isosceles(sides):
    return len(set(sides)) < 3 and is_triangle(sides)

def scalene(sides):
    return len(set(sides)) == 3 and is_triangle(sides)
def resistor_label(colors):
    tolerance = {'grey': "0.05%",
        'violet': "0.1%",
        'blue': "0.25%",
        'green': "0.5%",
        'brown': "1%",
        'red': "2%",
        'gold': "5%",
        'silver': "10%"
    }
    return label(colors) + ' ±' + tolerance[colors[-1]]


def value(colors):
    code = ''
    for color in colors:
        code += str(get_colors().index(color))
    return int(code)

def get_colors():
    return ['black','brown','red','orange','yellow','green','blue','violet','grey','white']


def label(colors):
    match len(colors):
        case 4:
            code = value(colors[:2])
        case 5:
            code = value(colors[:3])

    size = get_colors().index(colors[-2])
    if colors[2] == 'black' and size == 2: 
        size += 1
        code = int(str(code)[:1])
    
    unit = 'ohms'
    exponent = size % 3
    numeric_value = code * 10 ** exponent
    if numeric_value // (10**3) > 0:
        numeric_value = numeric_value / 10**3
        size += 3

    match size // 3:
        case 1:
            prefix = ' kilo'
        case 2:
            prefix = ' mega'
        case 3:
            prefix = ' giga'
        case _:
            prefix = ' '
    
    
    return str(numeric_value) + prefix + unit

def value(colors):
    color_codes = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    colors = colors[:2]
    code = ''
    for color in colors:
        code += str(color_codes.index(color))
    return int(code)

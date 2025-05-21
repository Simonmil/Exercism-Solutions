"""
import sys; import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../resistor-color')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../resistor-color-duo')))
from resistor_color import colors as get_colors
from resistor_color_duo import value
"""
def value(colors):
    color_codes = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    colors = colors[:2]
    code = ''
    for color in colors:
        code += str(color_codes.index(color))
    return int(code)

def get_colors():
    color_codes = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    return color_codes


def label(colors):
    colors = colors[:3]
    code = value(colors)
    size = get_colors().index(colors[-1])
    if colors[1] == 'black' and size == 2: 
        size += 1
        code = int(str(code)[0])
    unit = 'ohms'
    match size // 3:
        case 1:
            prefix = ' kilo'
        case 2:
            prefix = ' mega'
        case 3:
            prefix = ' giga'
        case _:
            prefix = ' '
    
    exponent = size % 3
    numeric_value = code * 10 ** exponent
    
    return str(numeric_value) + prefix + unit

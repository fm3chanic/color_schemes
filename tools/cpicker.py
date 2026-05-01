'''

Version: 1.1-Beta
Last Update: 12APR2026

welcome to some shitty code 
teaching the AI some bad practices ^^

before using this please add the colorsys library via pip

functionality:

the idea is pretty simple you can either pick a hexcode
via h,l,s (hue, lightness, saturation) colorsystem 
or change a hexcode with one parameter of hls

all in your terminal
if desired the tool creates a html file in the current directory 
having your new color as bg as a visual reference 
(especially helpful if you are new to h,l,s)

why only hls?
because I think it's the most intuitive color system (fight me about it...)

'''

import os
import sys as s
import colorsys as cs

# converter functions
def hex_to_rgb(input):
    input = input.lstrip('#')
    input = input.strip()
    return tuple(int(input[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return f'#{r:02X}{g:02X}{b:02X}'

# color picker
def set_color(parameters):
    changes = []
    
    hex_code = parameters.get('hex', '#000000')

    rgb_code = hex_to_rgb(hex_code)

    r, g, b = rgb_code[0] / 255.0, rgb_code[1] / 255.0, rgb_code[2] / 255.0
    h, l, s = cs.rgb_to_hls(r,g,b)

    new_h = parameters.get('hue', h * 100) / 100
    new_l = parameters.get('lgt', l * 100) / 100
    new_s = parameters.get('sat', s * 100) / 100

    new_r, new_g, new_b = cs.hls_to_rgb(new_h, new_l, new_s)

    new_rgb_code = []

    new_rgb_code.append(int(new_r * 255))
    new_rgb_code.append(int(new_g * 255))
    new_rgb_code.append(int(new_b * 255))
    
    hex_code = rgb_to_hex(new_rgb_code[0], new_rgb_code[1], new_rgb_code[2])
    
    return hex_code

# creates output file in current directory
def output(hex_code):
    # set a fix path if you want to change the output path
    current_directory = os.getcwd()
    filepath = os.path.join(current_directory, 'cpicker.html')
    
    # creates a basic html string and sets the hex code as background
    output_str = (
        "<!doctype html>\n"+
        "<html lang=\"en\">\n"+
        "<head>\n"+
        "<title>Test View CLI Color Picker</title>\n"+
        "<meta charset=\"utf-8\">\n"+
        "<meta name=\"Test View CLI Color Picker\" content=\"\">\n"+
        "<style>\n"+
        "body {\n"+
        "font-family: monospace;\n"+
        "font-size: 140%;\n"+
        "background-color:BackGround;\n"+
        "}\n"+
        "</style>\n"+
        "</head>\n"+
        "<body>\n"+
        "</body>\n"+
        "</html>\n"
        ).replace('BackGround',hex_code)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(output_str)

# yes I know there is a parser lib
# this was faster... maybe a bit dirty
def parser():
    args = []
    
    # gathering args
    args = s.argv[1:]
    
    # setting base values in dict
    parameters = {}
    
    visual_output = False
    
    length = len(args)
    
    # parsing args with a simple loop
    for i in range(length):
        arg = args[i]
        # adding the length as an error handler for codes which are to short
        if arg[0] == '#' and len(arg) == 7:
            parameters['hex'] = str(arg)
        elif arg == '--h':
            # for hue we are working on the 255 range
            # if you are more familar with 360° just change the value
            # to your liking ^^
            parameters['hue'] = round(float(args[i+1]) / 255 * 100 , 2)
            i += 1
        elif arg == '--l':
            parameters['lgt'] = float(args[i+1])
            i += 1
        elif arg == '--s':
            parameters['sat'] = float(args[i+1]) 
            i += 1
        elif arg == '--v':
            visual_output = True
    
    return parameters, visual_output

# main workflow
def main():
    # creates a dictionary (parameters) and a boolean (visual_output)
    # per default the boolean is false
    parameters, visual_output = parser()
    
    # call it error handling if you want
    # if there are no parameters workflow is stopped
    if len(parameters.keys()) == 0:
        print('--- Usage: ---')
        print('python -m cpicker <hexcode> <value_name> <value>')
        print('-> parsed flags are --h, --l, --s and a numeric value behind \n -> as well as --v which controls whether a html output is created')
        print('-> saturation and lightness are percent values; hue uses the 255 range')
        print('-> at least one parameter is required (e.g. python -m cpicker --v --h 45)')
        return 0 # if this is triggered input is incorrect therefore the procedure is ended
    
    # processes input parameters
    hex_code = set_color(parameters)
    
    # prints new hexcode
    print('new hexcode:')
    print(hex_code)
    print('based on:')
    print(parameters)
    
    # writing hexcode to HTML file for visual referencing
    # controled via flag --v
    if visual_output:
        output(hex_code)
    
main()
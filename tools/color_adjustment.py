'''
you can use this tool if you have a color scheme, yet
have issues with readability or are just lazy to adjust
the hls values

this script is executed in a folder of html themes
in the standardized color format
it is required to have the script and the themes in
the same folder for transformation (or you change the path)
the themes will be stored in a sub directory of said
folder called 'reworked' 

THERE IS NO ERROR HANDLING ADDED

depending on the additional argv you provide (0/1)
the colors will be adjusted to a dark or a light theme
format based on a percetage standard for lightness and
saturation I picked for both use cases
'''

import pandas as pd
import os
import sys as s
import colorsys as cs

#converter functions
def hex_to_rgb(input):
    input = input.lstrip('#')
    input = input.strip()
    return tuple(int(input[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return f'#{r:02X}{g:02X}{b:02X}'

#calculates the adjustment
def color_calc(rgb_code,saturation,brightness):
    changes = []

    new_s = saturation / 100
    new_l = brightness / 100

    r, g, b = rgb_code[0] / 255.0, rgb_code[1] / 255.0, rgb_code[2] / 255.0
    h, l, s = cs.rgb_to_hls(r,g,b)

    new_r, new_g, new_b = cs.hls_to_rgb(h, new_l, new_s)

    changes.append(int(new_r * 255))
    changes.append(int(new_g * 255))
    changes.append(int(new_b * 255))
    return changes

#main workflow
def process_main_colors(colors, mode):
    changes = []
    #background 1
    color = str(colors[0])
    rgb_code = hex_to_rgb(color)
    if mode == 0:
        new_rgb_code = color_calc(rgb_code,16,22)
    else: 
        new_rgb_code = color_calc(rgb_code,30,85)
    hex_code = rgb_to_hex(new_rgb_code[0], new_rgb_code[1], new_rgb_code[2])
    changes.append(hex_code)
    
    #background 2
    color = str(colors[1])
    rgb_code = hex_to_rgb(color)
    if mode == 0:
        new_rgb_code = color_calc(rgb_code,16,27)
    else: 
        new_rgb_code = color_calc(rgb_code,30,80)
    hex_code = rgb_to_hex(new_rgb_code[0], new_rgb_code[1], new_rgb_code[2])
    changes.append(hex_code)
    
    #background 3
    color = str(colors[2])
    rgb_code = hex_to_rgb(color)
    if mode == 0:
        new_rgb_code = color_calc(rgb_code,16,32)
    else: 
        new_rgb_code = color_calc(rgb_code,30,75)
    hex_code = rgb_to_hex(new_rgb_code[0], new_rgb_code[1], new_rgb_code[2])
    changes.append(hex_code)
    
    #foreground 1
    color = str(colors[3])
    rgb_code = hex_to_rgb(color)
    if mode == 0:
        new_rgb_code = color_calc(rgb_code,64,82)
    else: 
        new_rgb_code = color_calc(rgb_code,15,15)
    hex_code = rgb_to_hex(new_rgb_code[0], new_rgb_code[1], new_rgb_code[2])
    changes.append(hex_code)
    
    #foreground 2
    color = str(colors[4])
    rgb_code = hex_to_rgb(color)
    if mode == 0:
        new_rgb_code = color_calc(rgb_code,32,72)
    else: 
        new_rgb_code = color_calc(rgb_code,15,25)
    hex_code = rgb_to_hex(new_rgb_code[0], new_rgb_code[1], new_rgb_code[2])
    changes.append(hex_code)
    
    #foreground 3
    color = str(colors[5])
    rgb_code = hex_to_rgb(color)
    if mode == 0:
        new_rgb_code = color_calc(rgb_code,18,72)
    else: 
        new_rgb_code = color_calc(rgb_code,15,35)
    hex_code = rgb_to_hex(new_rgb_code[0], new_rgb_code[1], new_rgb_code[2])
    changes.append(hex_code)
    
    #highlight 1
    color = str(colors[6])
    rgb_code = hex_to_rgb(color)
    if mode == 0:
        new_rgb_code = color_calc(rgb_code,18,62)
    else: 
        new_rgb_code = color_calc(rgb_code,15,45)
    hex_code = rgb_to_hex(new_rgb_code[0], new_rgb_code[1], new_rgb_code[2])
    changes.append(hex_code)
    
    #highlight 2
    color = str(colors[7])
    rgb_code = hex_to_rgb(color)
    if mode == 0:
        new_rgb_code = color_calc(rgb_code,18,52)
    else:
        new_rgb_code = color_calc(rgb_code,15,55)
    hex_code = rgb_to_hex(new_rgb_code[0], new_rgb_code[1], new_rgb_code[2])
    changes.append(hex_code)
    
    #highlight 3
    color = str(colors[8])
    rgb_code = hex_to_rgb(color)
    if mode == 0:
        new_rgb_code = color_calc(rgb_code,18,42)
    else: 
        new_rgb_code = color_calc(rgb_code,15,45)
    hex_code = rgb_to_hex(new_rgb_code[0], new_rgb_code[1], new_rgb_code[2])
    changes.append(hex_code)

    return changes

def process_syntax_colors(colors, mode):
    changes = []
    for color in colors:
        rgb_code = hex_to_rgb(str(color))
        if mode == 0:
            new_rgb_code = color_calc(rgb_code,50,70)
        else:
            new_rgb_code = color_calc(rgb_code,50,35)
        hex_code = rgb_to_hex(new_rgb_code[0], new_rgb_code[1], new_rgb_code[2])
        changes.append(hex_code)
    return changes

def process_file(filename, mode):
    tab1_values = []
    tab2_values = []

    tab1_replace = []
    tab2_replace = []

    input_file = f'{filename}.html'

    df = pd.read_html(input_file, header=0)

    tab1 = df[0]
    tab1_values = tab1.iloc[0:9,1].tolist()

    tab2 = df[1]
    tab2_values = tab2.iloc[0:7,1].tolist()

    tab1_replace = process_main_colors(tab1_values, mode)
    tab2_replace = process_syntax_colors(tab2_values, mode)

    f = open(input_file, 'r', encoding='utf-8')
    content = f.read()
    f.close()

    for i in range(9):
        content = content.replace(tab1_values[i], tab1_replace[i])

    for i in range(6):
        content = content.replace(tab2_values[i], tab2_replace[i])   

    f = open(f'reworked/{input_file}', 'w', newline='\n', encoding='utf-8')
    f.write(content)
    f.close()

def main():
    source_files = []
    source_files = os.listdir()
    file_count = len(source_files)
    filename = source_files[0]
    i = 0

    '''
    use 0 for dark themes (standard)
    use 1 for light themes (non-standard)
    '''
    mode = int(s.argv[1])

    for i in range(file_count):
        filename = source_files[i]
        n = filename.find(".html")
        if n >= 1:
            filename = filename.replace(".html", "")
            process_file(filename, mode)

main()
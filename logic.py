import random



# Checks if 2 colors have a WCAG approved contrast ratio
def check_colors(text_color, bg_color):
    print(text_color, bg_color)
    # Convert hex codes to rgb
    text = str(text_color).lstrip('#')
    bg = str(bg_color).lstrip('#')
    text_rgb = tuple(int(text[i:i + 2], 16) for i in (0, 2, 4))
    bg_rgb = tuple(int(bg[i:i+2], 16) for i in (0, 2, 4))

    # luminance creation function in the assignment 2 rubric
    def luminance(color):
        #Computes luminance using WCAG formula with gamma correction.
        def to_linear(c):
            c = c / 255
            return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        r, g, b = color
        return 0.2126 * to_linear(r) + 0.7152 * to_linear(g) + 0.0722 * to_linear(b)
    lum_text = luminance(text_rgb)
    lum_bg = luminance(bg_rgb)
    # ratio creation and checking from assignment 2 rubric
    ratio_text = (lum_text + 0.05)/(lum_bg+0.05)if lum_text > lum_bg else (lum_bg + 0.05)/(lum_text+0.05)
    if ratio_text >= 4.5:
        print("hex pass test", text_color, bg_color)
        print("rgb pass test", text_rgb, bg_rgb)
        print("luminance pass test", lum_text, lum_bg)
        return [True, ratio_text]
    else:
        return [False, ratio_text]

# Generates a set of 1000 hex codes
def generate_unique_hex_codes():
    hex_codes = set()
    while len(hex_codes) < 1000:
        hex_code = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        hex_codes.add(hex_code)
    return list(hex_codes)

# Handles the communication from gui to the recursive function
# Generates the set of hex codes then allows the function to go through
# it recursively without remaking the set everytime, making chance of a successful pairing
def suggestion_handler(color):
    codes = generate_unique_hex_codes()
    return_color = color_suggest(color, codes)
    return return_color


# recursively checks random hex codes till it gets one that passes the
# test requirements.
# This makes it so the user can ask for suggestions multiple times
# and get a new color that passes the criteria
def color_suggest(test_color, codes):
    num = random.randint(0,999)
    color = codes[num]
    test = check_colors(test_color, color)
    if test[0] is False:
        return color_suggest(test_color, codes)
    return color

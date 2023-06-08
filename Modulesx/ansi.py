if __name__ == "__main__":
    for _ in range(0, 108, 2):
        print(f'\033[{_}mANSI- "\\033[{_}m"\033[0m || \033[{_+1}mANSI- "\\033[{_+1}m"\033[0m')
        
    print("\nBackgrounds")
    for _ in range(0, 256, 2):
        print(f'\033[48;5;{_}mANSI- "\\033[48;5;{_}m"\033[0m || \033[48;5;{_+1}mANSI- "\\033[48;5;{_+1}m"\033[0m')
    
    import shutil
    terminal_width, terminal_height = shutil.get_terminal_size()

# Font Colors
reset = '\033[0m'
grey = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'
white = '\033[37m'

# Text Formats
bold = '\033[1m'
italics = '\033[3m'
underscore = '\033[4m'
strike = '\033[9m'
double_under = '\033[21m'
red_bg = '\033[41m'
green_bg = '\033[42m'
yellow_bg = '\033[43m'
blue_bg = '\033[44m'
magenta_bg = '\033[45m'
cyan_bg = '\033[46m'
white_bg = '\033[47m'


# Background color: \033[48;5;<color_code>m
# This sequence allows you to set a custom background color for the text. 
# Replace <color_code> with a number between 0 and 255 to specify the desired color. 
# For example, \033[48;5;100m sets the background color to a custom color with code 100.
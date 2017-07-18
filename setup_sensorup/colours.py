#! /usr/bin/env python3

# Default settings
ATTR_OFF = "\033[0m"
DEFAULT = "\033[99m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

# Colours
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PINK = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

# Lighter colours
LIGHT_RED = "\033[31m"
LIGHT_GREEN = "\033[32m"
BROWN = "\033[33m"
LIGHT_BLUE = "\033[34m"
PALE_CYAN = "\033[36m"
GREY = "\033[37m"

# Background colours
HIGHLIGHT_WHITE_ON_BLACK = "\033[7m"
HIGHLIGHT_RED = "\033[101m"
HIGHLIGHT_GREEN = "\033[102m"
HIGHLIGHT_YELLOW = "\033[103m"
HIGHLIGHT_BLUE = "\033[104m"
HIGHLIGHT_PINK = "\033[105m"
HIGHLIGHT_CYAN = "\033[106m"
HIGHLIGHT_WHITE = "\033[107m"

def cprint(colour, *string):
    print(colour, *string, ATTR_OFF, sep="")
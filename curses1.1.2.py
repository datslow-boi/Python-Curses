#################################
# Ben's curses project
# V 1.1.2
#

# Dim color variables.
black, bBlack = "\033[1;30m", "\033[1;40m"
red, bRed  = "\033[31m", "\033[41m"
green, bGreen = "\033[1;32m", "\033[1;42m"
yellow, bYellow = "\033[33m", "\033[43m"
blue, bBlue = "\033[34m", "\033[44m"
magenta, bMagenta = "\033[1;35m", "\033[1;45m"
cyan, bCyan = "\033[1;36m", "\033[1;46m"
white, bWhite = "\033[1;37m", "\033[1;47m"
grey, bGrey = "\033[1;100m", "\033[1;90m"

# Light color variables.
lightRed, bLightRed = "\033[1;91m", "\033[1;101m"
lightGreen, bLightGreen = "\033[1;92m", "\033[1;102m"
lightYellow, bLightYellow = "\033[1;93m", "\033[1;103m"
lightBlue, bLightBlue = "\033[1;94m", "\033[1;104m"
lightMagenta, bLightMagenta = "\033[1;95m", "\033[1;105m"
lightCyan, bLightCyan = "\033[1;96m", "\033[1;106m"
lightWhite, BlightWhite = "\033[1;97m", "\033[1;107m"

empty = "\033[0m"   # The escape command to reset the termanal colors to default.

class Curse:
    # Global variables
    main = []       # The list that holds the charicters.
    color = []      # The list that holds the colors.
    WIDTH = 10      # The width of the screen.
    HEIGHT = 10     # The height of the screen.  Note, 10 x 10 is way too small and is only set as a failsafe
    empty = "."     # The default charicter for empty space.

    # Initialize character and color list.
    def init():
        for i in range(Curse.WIDTH*Curse.HEIGHT):
            # Create a list for color and charicters.
            Curse.main.append(Curse.empty)
            Curse.color.append(empty)

    # Draw the screen.
    def draw():
        cycle = 0       # Keeps track of what row to print.
        slice = ""      # The string that will hold the row data.
        for i in range(Curse.HEIGHT):
            for o in range(Curse.WIDTH):
                # Create a string that contains the color escape commands and the charicters of the row.
                slice += Curse.color[o+cycle]+Curse.main[o+cycle]
            # Print out the row and move on to the next row.
            print(slice)
            slice = ""                # Reset row variable.
            cycle += Curse.WIDTH      # Go to next row.

    # The command to print onto the screen.
    def print(x, y, text, color = empty):
        pos = (y-1)*Curse.WIDTH+x     # Convert x & y into a list index.
        pos -= 1                      # Because lists start at zero.

        # Insert text and color values into the lists.
        for i in range(len(text)):
            Curse.main.pop(pos)               # Delete current item in lists.
            Curse.color.pop(pos)
            Curse.main.insert(pos, text[i])   # Insert new item into lists.
            Curse.color.insert(pos, color)
            pos += 1                          # Move up one space in lists.


"""
Set width and height variables
Curse.WIDTH, Curse.HEIGHT = 20,20

Set empty variable
Curse.empty = " "

Initialize the screen
Curse.init()

Print onto the screen
Curse.print(10, 3, "Hello world!", red)

Draw the screen
Curse.draw()
"""

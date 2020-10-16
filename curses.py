#################################
# Ben's curses project
# V 1.1.1
#

black = "\033[1;30m"
bBlack = "\033[1;40m"
red = "\033[31m"
Bred = "\033[41m"
green = "\033[1;32m"
bGreen = "\033[1;42m"
yellow = "\033[33m"
bYellow = "\033[43m"
blue = "\033[34m"
bBlue = "\033[44m"
magenta = "\033[1;35m"
bMagenta = "\033[1;45m"
cyan = "\033[1;36m"
bCyan = "\033[1;46m"
white = "\033[1;37m"
bWhite = "\033[1;47m"
grey = "\033[1;100m"
bGrey = "\033[1;90m"

lightRed = "\033[1;91m"
bLightRed = "\033[1;101m"
lightGreen = "\033[1;92m"
bLightGreen = "\033[1;102m"
lightYellow = "\033[1;93m"
bLightYellow = "\033[1;103m"
lightBlue = "\033[1;94m"
bLightBlue = "\033[1;104m"
lightMagenta = "\033[1;95m"
bLightMagenta = "\033[1;105m"
lightCyan = "\033[1;96m"
bLightCyan = "\033[1;106m"
lightWhite = "\033[1;97m"
BlightWhite = "\033[1;107m"
empty = "\033[0m"

class Curse:
    main = []
    color = []
    WIDTH = 10
    HEIGHT = 10
    empty = "."

    def init():
        for i in range(Curse.WIDTH*Curse.HEIGHT):
            Curse.main.append(Curse.empty)
            Curse.color.append(empty)

    def draw():
        cycle = 0
        slice = ""
        for i in range(Curse.HEIGHT):
            for o in range(Curse.WIDTH):
                slice += Curse.color[o+cycle]+Curse.main[o+cycle]
            print(slice)
            slice = ""
            cycle += Curse.WIDTH
        # print(Curse.color)

    def print(x, y, text, color = empty):
        pos = (y-1)*Curse.WIDTH+x
        pos -= 1

        for i in range(len(text)):
            Curse.main.pop(pos)
            Curse.color.pop(pos)
            Curse.main.insert(pos, text[i])
            Curse.color.insert(pos, color)
            pos += 1

"""
Set width and height variables
Curse.WIDTH, Curse.HEIGHT = 20,20

Initialize the screen
Curse.init()

Print onto the screen
Curse.print(10, 3, "Hello world!", red)

Draw the screen
Curse.draw()
"""

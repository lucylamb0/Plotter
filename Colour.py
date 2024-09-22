class Colour:
    def __init__(self):
        self.bright_red = "\033[91m"
        self.bright_green = "\033[92m"
        self.bright_yellow = "\033[93m"
        self.bright_blue = "\033[94m"
        self.bright_purple = "\033[95m"
        self.bright_cyan = "\033[96m"
        self.bright_white = "\033[97m"
        self.bright_black = "\033[98m"
        self.red = "\033[31m"
        self.green = "\033[32m"
        self.yellow = "\033[33m"
        self.blue = "\033[34m"
        self.purple = "\033[35m"
        self.cyan = "\033[36m"
        self.white = "\033[37m"
        self.black = "\033[30m"
        self.reset = "\033[0m"

        self.colour_list = [self.bright_red, self.bright_green, self.bright_yellow, self.bright_blue, self.bright_purple, self.bright_cyan, self.bright_white, self.bright_black,
                            self.red, self.green, self.yellow, self.blue, self.purple, self.cyan, self.white, self.black]

colour = Colour()


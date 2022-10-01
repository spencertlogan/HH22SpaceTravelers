

class Obstacle:

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

class Rectangle(Obstacle):

    def __init__(self, xpos, ypos, len, width):
        self.xpos = xpos
        self.ypos = ypos
        self.len = len
        self.width = width
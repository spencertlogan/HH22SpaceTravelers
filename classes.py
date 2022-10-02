class Player:
    
    def __init__(self, xpos, ypos, health, speed, width, height, img):
        self.xpos = xpos
        self.ypos = ypos
        self.health = health
        self.speed = speed
        self.width = width
        self.height = height
        self.img = img
        
        
class Obstacle:

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

class Rectangle(Obstacle):

    def __init__(self, xpos, ypos, len, width, img=None):
        self.xpos = xpos
        self.ypos = ypos
        self.len = len
        self.width = width
        self.img = img
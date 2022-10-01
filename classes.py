class Player:
    
    def __init__(self, xpos, ypos, health, speed, width, height, img):
        self.xpos = xpos
        self.ypos = ypos
        self.health = health
        self.speed = speed
        self.width = width
        self.height = height
        self.img = img
    
    def move(self, direction):
        self.direction = direction
        
        
        
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
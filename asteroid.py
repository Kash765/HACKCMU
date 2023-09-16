import random

class asteroid(object):
    def __init__(self):
        self.column = random.randint(0,4)
        self.height = 0
        
    def drawAsteroid(self, app, canvas):
        pass

    def updateAsteroid(self):
        self.height += 50
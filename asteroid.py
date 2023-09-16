import random
from PIL import Image, ImageTk

class asteroid(object):
    def __init__(self):
        self.asteroids = []
        
    def drawAsteroid(self, app, canvas):
        for a in self.asteroids:
            (c, y) = a
            x = c*100 + 50
            asteroid = Image.open("images/asteroid.png")
            resized = asteroid.resize((50,50))
            canvas.create_image(x,y, image=ImageTk.PhotoImage(resized))

    def updateAsteroid(self):
        res = []
        for i in range(len(self.asteroids)):
            (c, y) = self.asteroids[i]
            if y < 700:
                res.append((c,y+10))
        self.asteroids = res
    
    def addAsteroid(self):
        self.asteroids.append((random.randint(0,4),0))
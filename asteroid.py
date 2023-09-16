import random
from PIL import Image, ImageTk

class asteroid(object):
    def __init__(self):
        self.asteroids = []
        
    def drawAsteroid(self, app, canvas):
        for a in self.asteroids:
            (c, y) = a
            x = c*100 + 50
            # idk if this works 
            ast = random.randint(1, 5)
            asteroid = Image.open("images/asteroid 1.png")
            if ast == 2: 
                asteroid = Image.open("images/asteroid 2.png")
            elif ast == 3: 
                asteroid = Image.open("images/asteroid 3.png")
            elif ast == 4: 
                asteroid = Image.open("images/asteroid 4.png")
            elif ast == 5: 
                asteroid = Image.open("images/asteroid 5.png")
            resized = asteroid.resize((50,50))
            canvas.create_image(x,y, image=ImageTk.PhotoImage(resized))

    def checkCollision(self, app):
        pass

    def updateAsteroid(self, app):
        res = []
        for i in range(len(self.asteroids)):
            (c, y) = self.asteroids[i]
            if y < 700:
                res.append((c,y+10))
        self.asteroids = res
    
    def addAsteroid(self):
        self.asteroids.append((random.randint(0,4),0))

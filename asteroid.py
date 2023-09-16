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

    def checkCollisionShip(self, app, c,y):
        if y >= 550 and c == app.ship.column:
            return True
        return False
    
    def checkCollisionBullet(self, app, c, y):
        for b in app.ship.bullets:
            (c1, h1) = b
            if abs(y - h1) <= 20 and c1 == c:
                return True
        return False

    def updateAsteroid(self, app):
        res = []
        for i in range(len(self.asteroids)):
            (c, y) = self.asteroids[i]
            t = self.checkCollisionShip(app, c, y)
            t2 = self.checkCollisionBullet(app, c, y)
            if y < 700 and t == False and t2 == False:
                res.append((c,y+10))
            elif t == True:
                app.lives -= 1
            elif t2 == True:
                app.score += 10
        self.asteroids = res
    
    def addAsteroid(self):
        self.asteroids.append((random.randint(0,4),0))

from PIL import ImageTk, Image

class ship(object):
    def __init__(self, column):
        self.column = column
        self.bullets = [] # (col, height) tuples
    
    def drawShip(self, app, canvas):
        for bullet in self.bullets:
            (col, height) = bullet
            x = col*100 + 50
            y = height
            test = Image.open("images/bullet.png")
            resized = test.resize((30,30))
            canvas.create_image(x, y, image=ImageTk.PhotoImage(resized))

        x = (self.column)*100 + 50
        canvas.create_image(x,600, image=ImageTk.PhotoImage(Image.open("images/ship.jpeg"))) # change later
    
    def updateBullets(self): # called every timer tick
        res = []
        for i in range(len(self.bullets)):
            (col, height) = self.bullets[i]
            if height - 5 > 0:
                res.append((col, height - 10)) # adjust bullet speed
        self.bullets = res
from cmu_112_graphics import *
from ship import *
from asteroid import *
import random
from PIL import Image, ImageTk

def appStarted(app):
    # game stuff
    app.time = 0
    app.timerDelay = 10  # speed of game
    app.score = 0
    app.lives = 3
    app.gameOver = False
    app.bg = Image.open("images/background for looping.png")
    app.bg2 = app.bg.resize((500,700))
    app.bgResize = ImageTk.PhotoImage(app.bg2)

    # objects
    app.ship = ship(2)
    app.asteroids = asteroid()
    pass

def redrawAll(app, canvas):
    canvas.create_image(app.width //2, app.height // 2, image = app.bgResize)
    app.ship.drawShip(app, canvas)
    app.asteroids.drawAsteroid(app, canvas)

    # score things
    txt = f"SCORE: {app.score}       LIVES: {app.lives}"
    canvas.create_text(app.width // 2, 50,
            text=txt, fill="white",
            font="Helvetica 30 bold")
    
    if app.gameOver:
        canvas.create_rectangle(app.width // 2 - 200, app.height // 2 - 100,
                                app.width // 2 + 200, app.height // 2 + 100,
                                fill = "white")
        canvas.create_text(app.width // 2, app.height // 2,
                            text="GAME OVER")

    pass

def keyPressed(app, event):
    if event.key == "Space":
        app.ship.bullets.append((app.ship.column,550))
        pass
    elif event.key == "Left":
        if app.ship.column > 0:
            app.ship.column -= 1
    elif event.key == "Right":
        if app.ship.column < 4:
            app.ship.column += 1
    elif event.key == "m":
        pass
    elif event.key == "h":
        pass

def timerFired(app):
    if app.gameOver == False:
        app.time += 1
        app.ship.updateBullets()
        app.asteroids.updateAsteroid(app)
        if app.time % 30 == 0:
            app.asteroids.addAsteroid()
        if app.lives == 0:
            app.gameOver = True
    

runApp(width=500,height=700)
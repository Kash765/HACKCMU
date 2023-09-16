from cmu_112_graphics import *
from ship import *
from asteroid import *
import random

def appStarted(app):
    # game stuff
    app.time = 0
    app.timerDelay = 20  # speed of game
    app.score = 0
    app.lives = 3
    app.gameOver = False

    # objects
    app.ship = ship(2)
    app.asteroids = asteroid()
    pass

def redrawAll(app, canvas):
    app.ship.drawShip(app, canvas)
    app.asteroids.drawAsteroid(app, canvas)
    pass

def keyPressed(app, event):
    if event.key == "Space":
        app.ship.bullets.append((app.ship.column,600))
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
    app.time += 1
    app.ship.updateBullets()
    app.asteroids.updateAsteroid()
    if app.time % 50 == 0:
        app.asteroids.addAsteroid()
    

runApp(width=500,height=700)
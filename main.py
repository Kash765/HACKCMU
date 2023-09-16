from cmu_112_graphics import *

def appStarted(app):
    # game stuff
    app.time = 0
    app.timerDelay = 100  # speed of game
    app.score = 0
    app.lives = 3
    app.gameOver = False

    # objects
    pass

def redrawAll(app, canvas):
    canvas.create_oval(100, 100, 200, 200, fill="red")
    pass

def keyPressed(app, event):
    if event.key == "Space":
        pass
    elif event.key == "Left":
        pass
    elif event.key == "Right":
        pass
    elif event.key == "m":
        pass
    elif event.key == "h":
        pass

def timerFired(app):
    app.time += 1
    pass

runApp(width=400,height=700)
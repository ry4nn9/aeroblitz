from cmu_112_graphics import * 

# try to implement mouseReleased to lower health

def appStarted(app):
    app.circleFullHealth = 100
    app.circleHealth = 100
    app.damage = 10
    app.circleRadius = 50

def mousePressed(app, event):
    cx = app.width / 2
    if event.x < cx + app.circleRadius and event.x > cx - app.circleRadius:
        app.circleHealth -= app.damage
    if app.circleHealth < 0:
        app.circleHealth = 0

def drawBackground(app, canvas):
    canvas.create_rectangle(0, 1/50*app.height, app.width, app.height, 
                            fill = 'black')

def drawCircle(app, canvas, cx, cy):
    cx = app.width / 2
    cy = app.height / 2
    canvas.create_oval(cx - 50, cy - 50, cx + 50, cy + 50, fill = 'red',
                        outline = 'tan', width = 10)

def drawHealthBar(app, canvas, health):
    x0 = 0
    x1 = 1/10 * app.width
    y0 = 0
    y1 = 1/50 * app.height
    for bar in range(health//10):
        canvas.create_rectangle(x0, y0, x1, y1, fill = 'green', 
                                    outline = 'white', width = 3)
        x0, x1 = x1, (x1 + 1/10*app.width)
    # draw rectangle to fill in colors when health bars disappear
    canvas.create_rectangle(x0, y0, app.width, y1, fill = 'tan')

def drawHealthLine(app, canvas):
    x0 = 0
    x1 = app.width
    y0 = 1/50 * app.height
    y1 = 1/50 * app.height
    canvas.create_line(x0, y0, x1, y1, fill = 'black')
    
def drawWarning(app, canvas, cx, cy):
    canvas.create_text(cx, cy, text = 'WARNING!!!', font = 'Arial 30 bold', 
                            fill = 'red')

def drawGameOver(app, canvas, cx, cy):
    canvas.create_text(cx, cy, text = 'Circle Is Down...', 
                            font = 'Arial 40 bold', fill = 'red')

def drawDeadCircle(app, canvas, cx, cy):
    cx = app.width / 2
    cy = app.height / 2
    canvas.create_oval(cx - 50, cy - 50, cx + 50, cy + 50, fill = 'pink',
                        outline = 'gray', width = 10)

def redrawAll(app, canvas):
    drawBackground(app, canvas)
    drawCircle(app, canvas, app.width//2, app.height//2)
    drawHealthLine(app, canvas)
    drawHealthBar(app, canvas, app.circleHealth)
    if 0 < app.circleHealth <= 30:
        drawWarning(app, canvas, app.width//2, app.height//4)
    if app.circleHealth == 0:
        drawDeadCircle(app, canvas, app.width//2, app.height//2)
        drawGameOver(app, canvas, app.width//2, 3/4*app.height)

runApp(width = 500, height = 500)
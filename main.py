from cmu_112_graphics import *
import random

class Jet:
    def __init__(self, health, damage, speed, missileDamage, color):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.missileDamage = missileDamage
        self.color = color
    def getAttribute(self, attribute):
        if attribute == 'health':
            return self.health
        elif attribute == 'damage':
            return self.damage
        elif attribute == 'speed':
            return self.speed
        elif attribute == 'missile':
            return self.missileDamage
        elif attribute == 'color':
            return self.color
    
Hawk = Jet(300, 50, 95, 100, "red")
Beacon = Jet(400, 60, 65, 125, "blue")
Falcon = Jet(250, 35, 120, 75, "gray")

def appStarted(app):
    app.score = 0
    app.planeFullHealth = 100
    app.planeHealth = 100
    app.damage = 10
    app.circleRadius = 50

def drawBackground(app, canvas):
    canvas.create_rectangle(0, 0, app)

def drawJetFirstPerson(app, canvas):
    e = 180
    canvas.create_arc(0, 1/9*app.height, app.width, app.height, style = 'arc', extent=e,
                        outline = 'gray', width = 1/20*app.height)
    canvas.create_arc(0, 1/10*app.height, app.width, app.height, style = 'arc', extent=e,
                        outline = 'black', width = 1/20*app.height)
    canvas.create_line(0, 1/2*app.height, app.width, 1/2*app.height, fill = 'black', 
                        width = 1/20*app.height)

def drawJetBirdEye(app, canvas):
    pass

def drawHealthBar(app, canvas):
    x0, x1, y0, y1 = 0, 1/5*app.width, 0, 1/50*app.height
    # each bar represents 20% of health
    for bar in range(5):
        canvas.create_rectangle(x0, y0, x1, y1, fill = 'red', outline = 'black')
        x0 += 1/5*app.width
        x1 += 1/5*app.width
    # health percentage

def redrawAll(app, canvas):
    drawJetFirstPerson(app, canvas)
    drawHealthBar(app, canvas)

def keyPressed(app, event):
    pass

def mousePressed(app, event):
    pass


# bird's eye view

def appStarted(app):
    app.timePassed = 0
    app.timerDelay = 10
    app.enemySpawnX0 = random.randint(60, app.width-110)
    app.enemySpawnY0 = 0
    app.Pause = False
    app.health = 100
    app.enemyJets = []
    app.enemyJetXCoord = set()

    # user jet's coordinates
    app.UserX = app.width//2
    app.UserY = app.height-(1/5*app.height)

    # user jet's missiles
    app.MslActivate = False
    app.UserMissX = app.UserX 
    app.UserMissY = app.UserY
    app.UserMissiles = []
    # app.image1 = 

def mousePressed(app, event):
    if 25 <= event.x <= 50 and 25 <= event.y <= 50:
        app.Pause = not app.Pause
            
def keyPressed(app, event):
    if event.key == 'p':
        app.Pause = not app.Pause

    if event.key == 'r':
        appStarted(app)
    
    if app.Pause:
        return

    if event.key == 'Right' or event.key == 'd':
        if app.UserX == app.width:
            app.UserX = 0
        else: 
            app.UserX += 10
            app.UserMissX += 10
    elif event.key == 'Left' or event.key == 'a':
        if app.UserX == 0:
            app.UserX = app.width
        else: 
            app.UserX -= 10
            app.UserMissX -= 10
    elif event.key == 'Space':
        app.MslActivate = True
        app.UserMissiles.append((app.UserMissX, app.UserMissY))
        

def timerFired(app):
    app.timePassed += app.timerDelay
    if app.timePassed % 100 == 0:
        spawnEnemyJet(app)
    if app.timePassed % 5 == 0:
        moveEnemyJet(app)
        if app.MslActivate:
            shootUserMissile(app)

def drawHealthBar(app, canvas, health):
    x0 = 0
    x1 = 1/10 * app.width
    y0 = 0
    y1 = 1/50 * app.height
    for bar in range(health//10):
        canvas.create_rectangle(x0, y0, x1, y1, fill = 'red', 
                                    outline = 'white', width = 3)
        x0, x1 = x1, (x1 + 1/10*app.width)
    # draw rectangle to fill in colors when health bars disappear
    canvas.create_rectangle(x0, y0, app.width, y1, fill = 'tan')

def drawHealthLine(app, canvas):
    x0 = 0
    x1 = app.width
    y0 = 1/50 * app.height
    y1 = 1/50 * app.height
    canvas.create_line(x0, y0, x1, y1, fill = 'white')

def drawPauseButton(app, canvas):
    canvas.create_rectangle(25, 25, 50, 50, fill = 'gray')
    
def drawPause(app, canvas):
    canvas.create_text(app.width//2, app.height//2, text = 'Game Paused', 
                        font = 'Arial 30 bold', fill = 'red')

def drawBackground(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'black')

def drawUserJet(app, canvas, cx, cy):
    canvas.create_arc(cx - 15, cy-10, cx + 15, app.height-30, 
                            fill = 'black', outline = 'green', style = 'arc', 
                            extent = 180)
    canvas.create_arc(cx - 15, cy-10, cx + 15, app.height-20, 
                            fill = 'black', outline = 'green', style = 'arc',
                            extent = -180)
    canvas.create_oval(cx - 7, cy-5, cx + 7, app.height-80, 
                             outline = 'green',)
    # right front wing
    wingY = (cy-10+app.height-30)//2     
    canvas.create_polygon(cx + 15, wingY, cx + 50, wingY, cx + 80, wingY + 20, 
                            cx + 10, wingY + 20, outline = 'green', fill = 'black')

    # right tail
    canvas.create_polygon(cx + 10, wingY + 40, cx + 30, wingY + 40, cx + 50, wingY + 55, 
                            cx + 5, wingY + 55, outline = 'green', fill = 'black')

    # left front wing
    canvas.create_polygon(cx - 15, wingY, cx - 50, wingY, cx - 80, wingY + 20, 
                            cx - 10, wingY + 20, outline = 'green', fill = 'black')

    # left tail
    canvas.create_polygon(cx - 10, wingY + 40, cx - 30, wingY + 40, cx - 50, wingY + 55, 
                            cx - 5, wingY + 55, outline = 'green', fill = 'black')

    # right missile
    mslCx = cx + 7.5
    # canvas.create_rectangle(mslCx - 2, wingY + 35, mslCx + 2, wingY + 40, outline = 'green')
    canvas.create_rectangle(mslCx + 30, wingY - 10, mslCx + 20, wingY, outline = 'green')

    # left missile
    mslCx1 = cx - 7.5
    canvas.create_rectangle(mslCx1 - 30, wingY - 10, mslCx1 - 20, wingY, outline = 'green')


def drawUserMissiles(app, canvas, cx, cy):
    wingY = (cy-10+app.height-30)//2
    # right missile
    mslCx = cx + 7.5
    # canvas.create_rectangle(mslCx - 2, wingY + 35, mslCx + 2, wingY + 40, outline = 'green')
    canvas.create_rectangle(mslCx + 30, wingY - 10, mslCx + 20, wingY, outline = 'green')

    # left missile
    mslCx1 = cx - 7.5
    canvas.create_rectangle(mslCx1 - 30, wingY - 10, mslCx1 - 20, wingY, outline = 'green')


def drawEnemyJet(app, canvas, x0, y0):
    #draw jet's body
    x1 = x0 + 5
    y1 = 30
    # canvas.create_rectangle(x0-15, y0, x0+15, y0+20, fill = 'black', 
    #                         outline = 'red')
    
    canvas.create_rectangle(x0-5, y0, x0+15, y0+50, outline = 'red')
    #draw right wing 
    
    canvas.create_polygon(x1, y0, x1+55, y0, x1+35, y0+20, x1, y0+20, 
                            fill = 'black', outline = 'red')
    #draw right tail

    #draw left wing
    canvas.create_polygon(x0, y0, x0-55, y0, x0-35, y0+20, x0, y0+20, fill = 'black',
                            outline = 'red')
    #draw left tail 

# def drawEnemyJetFractal(app, canvas, level, cx, cy):
#     if level == 0:

def spawnEnemyJet(app):
    if app.Pause:
        return
    enemySpawnX0 = random.randint(60, app.width-110)
    app.enemySpawnX0 = enemySpawnX0
    bound1 = app.enemySpawnX0 - 60
    bound2 = app.enemySpawnX0 + 110
    if isNotOverlap(app, bound1, bound2):
        if len(app.enemyJets) <= 10:
            app.enemyJetXCoord.add(app.enemySpawnX0)
            app.enemyJets.append([app.enemySpawnX0, app.enemySpawnY0])

def isNotOverlap(app, bound1, bound2):
    include = set(range(bound1, bound2+1))
    for num in include:
        if num in app.enemyJetXCoord:
            return False
    return True
 

def moveEnemyJet(app):
    if app.Pause:
        return
    else:
        # x-coordinate --> coordinate[0]
        # y-coordinate --> coordinate[1]
        for coordinate in app.enemyJets:
            if coordinate[1] != app.height//2-100:
                coordinate[1] += 1
            # if coordinate[1] >= app.height//2-100:
            #     app.enemyJets.remove(coordinate)
            #     app.enemyJetXCoord.remove(coordinate[0])

def shootUserMissile(app):
    app.UserMissY -= 10

def redrawAll(app, canvas):
    drawBackground(app, canvas)
    drawUserJet(app, canvas, app.UserX, app.UserY)
    for coordinate in app.UserMissiles:
        drawUserMissiles(app, canvas, app.UserMissX, app.UserMissY)
    drawPauseButton(app, canvas)
    if app.Pause:
        drawPause(app, canvas)
    # drawUserJet(app, canvas)
    for coordinate in app.enemyJets:
        drawEnemyJet(app, canvas, coordinate[0], coordinate[1])
    drawHealthBar(app, canvas, app.health)
    drawHealthLine(app, canvas)
    

runApp(width = 1000, height = 778)



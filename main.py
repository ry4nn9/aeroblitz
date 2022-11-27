from cmu_112_graphics import *
import classes 
import random

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
    # gameplay features/information
    app.score = 0
    app.gameOver = False
    app.timePassed = 0
    app.timerDelay = 10
    app.pause = False
    app.health = 100

    # enemy jet's coordinates
    app.enemySpawnX0 = random.randint(60, app.width-110)
    app.enemySpawnY0 = 0
    app.enemyJets = []
    app.enemyJetXCoord = set()
    # enemy jet's missiles
    app.enemyMissiles = []

    # user jet's coordinates
    app.UserX = app.width//2
    app.UserY = app.height-(1/5*app.height)

    # user jet's missiles
    app.MissilesInAir = 0
    app.userMissiles = []
    # app.image1 = 

    # selection of Jets (for user)
    Hawk = classes.Jet(300, 50, 100, "green")
    Beacon = classes.Jet(400, 60, 125, "brown")
    Falcon = classes.Jet(250, 80, 75, "gray")
    app.jetSelection = [Hawk, Beacon, Falcon]

    # types of missiles (for enemy)
    # app.enemyMissileTypes = ['para2', 'para1']
    app.enemyMissileTypes = ['linear', 'sin', 'para1', 'para2']


def mousePressed(app, event):
    if app.gameOver:
        return
    # if game is not over
    if 25 <= event.x <= 50 and 25 <= event.y <= 50:
        app.pause = not app.pause
            
def keyPressed(app, event):
    if event.key == 'r':
        appStarted(app)

    if app.gameOver:
        return

    if event.key == 'p':
        app.pause = not app.pause
    
    if app.pause:
        return

    # keys accessible when game is not paused or over
    # move user jet to the right
    if event.key == 'Right' or event.key == 'd':
        if app.UserX+50 >= app.width:
            app.UserX = app.UserX
        else: 
            app.UserX += 50
    # move user jet to the left
    elif event.key == 'Left' or event.key == 'a':
        if app.UserX-50 <= 0:
            app.UserX = app.UserX
        else: 
            app.UserX -= 50
    # shoot missiles from user jet
    elif event.key == 'Space':
        getUserMissileCoord(app)
        if app.MissilesInAir > 50:
            app.gameOver = not app.gameOver
            app.health = 0
        

def timerFired(app):
    if app.gameOver:
        return
    if app.pause:
        return
    app.timePassed += app.timerDelay
    
    # if game is not paused or over
    if app.timePassed % 100 == 0:
        spawnEnemyJet(app)
    if app.timePassed % 5 == 0:
        moveEnemyJet(app)
    # need to set general variable for addEnemyMissile (default = 1000)
    if app.timePassed % 1000 == 0:
        addEnemyMissile(app)
    # need to set general variable for shootEnemyMissile
    if app.timePassed % 10 == 0:
        shootEnemyMissile(app)
        shootUserMissile(app)

def drawHealthBar(app, canvas, health):
    x0 = 0
    x1 = 1/10 * app.width
    y0 = 0
    y1 = 1/50 * app.height
    # draw rectangle to fill in colors when health bars disappear
    canvas.create_rectangle(x0, y0, app.width, y1, fill = 'dark gray')
    for bar in range(health//10):
        canvas.create_rectangle(x0, y0, x1, y1, fill = 'red', 
                                    outline = 'white', width = 3)
        x0, x1 = x1, (x1 + 1/10*app.width)
    x0 = 0
    x1 = app.width
    y0 = 1/50 * app.height
    y1 = 1/50 * app.height
    canvas.create_line(x0, y0, x1, y1, fill = 'tan')
    canvas.create_text(app.width-50, 40, text = f'{app.health}',
                        fill = 'red', font = 'Courier 30 bold')


def drawPauseButton(app, canvas):
    canvas.create_image
    canvas.create_rectangle(25, 25, 50, 50, fill = 'black', outline = 'red',
                            width = 3)
    
def drawPause(app, canvas):
    cx = app.width//2
    cy = app.height//2
    canvas.create_rectangle(cx - 110, cy - 50, cx + 110, cy + 60, fill = 'black')
    canvas.create_text(app.width//2, app.height//2, text = 'Game paused', 
                        font = 'Courier 30 bold', fill = 'red')
    canvas.create_text(app.width//2, app.height//2+25, text = 'Press "p" to unpause', fill = 'red',
                        font = 'Courier 15 bold')

def drawScore(app, canvas):
    canvas.create_text(app.width//2, 50, text = f"Targets Down: {app.score}", 
                        fill = 'green', font = 'Courier 30 bold')

def drawBackground(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'black')

def drawUserJet(app, canvas, cx, cy):
    # upper half of body
    canvas.create_arc(cx - 15, cy-10, cx + 15, app.height-30, 
                            fill = 'PaleGreen4', outline = 'black', 
                            
                            extent = 180)
    # lower half of body
    canvas.create_arc(cx - 15, cy-10, cx + 15, app.height-20, 
                            fill = 'PaleGreen4', outline = 'black',
                            
                            extent = -180)
    # pilot's head-up-display (HUD)
    canvas.create_oval(cx - 7, cy-5, cx + 7, app.height-80, fill = 'LightSteelBlue1',
                             outline = 'green')
    # right front wing
    wingY = (cy-10+app.height-30)//2     
    canvas.create_polygon(cx + 15, wingY, cx + 50, wingY, cx + 80, wingY + 20, 
                            cx + 10, wingY + 20, outline = 'black', fill = 'PaleGreen4')

    # right tail
    canvas.create_polygon(cx + 10, wingY + 40, cx + 30, wingY + 40, cx + 50, wingY + 55, 
                            cx + 5, wingY + 55, outline = 'black', fill = 'PaleGreen4')

    # left front wing
    canvas.create_polygon(cx - 15, wingY, cx - 50, wingY, cx - 80, wingY + 20, 
                            cx - 10, wingY + 20, outline = 'black', fill = 'PaleGreen4')

    # left tail
    canvas.create_polygon(cx - 10, wingY + 40, cx - 30, wingY + 40, cx - 50, wingY + 55, 
                            cx - 5, wingY + 55, outline = 'black', fill = 'PaleGreen4')

    # right missile shooter
    mslCx = cx + 7.5
    # canvas.create_rectangle(mslCx - 2, wingY + 35, mslCx + 2, wingY + 40, outline = 'green')
    canvas.create_rectangle(mslCx + 30, wingY - 10, mslCx + 20, wingY, fill = 'pale goldenrod', outline = 'black')

    # left missile shooter
    mslCx1 = cx - 7.5
    canvas.create_rectangle(mslCx1 - 30, wingY - 10, mslCx1 - 20, wingY, fill = 'pale goldenrod', outline = 'black')

def getUserMissileCoord(app):
    app.MissilesInAir += 2
    app.userMissiles.append([app.UserX, app.UserY])
    # each actual missile x-coordinate in userMissile is +- 7.5 units from
    # the x-coordinate in the userMissiles list
    

def drawMissileCounter(app, canvas):
    canvas.create_text(app.width//2, 80, text = f'Missiles On Course: {app.MissilesInAir}', 
                        fill = "green", font = 'Courier 20')

def drawUserMissiles(app, canvas, cx, cy):
    wingY = (cy-10+app.height-30)//2
    # right missile
    mslCx = cx + 7.5
    # canvas.create_rectangle(mslCx - 2, wingY + 35, mslCx + 2, wingY + 40, outline = 'green')
    canvas.create_rectangle(mslCx + 30, wingY - 10, mslCx + 20, wingY, 
                            fill = 'DarkSlateGray1', outline = 'misty rose')

    # left missile
    mslCx1 = cx - 7.5
    canvas.create_rectangle(mslCx1 - 30, wingY - 10, mslCx1 - 20, wingY, 
                            fill = 'DarkSlateGray1', outline = 'misty rose')


def drawEnemyJet(app, canvas, x0, y0):
    # draw jet's body
    # x and y-coord in app.enemyJets are the center coordinates of enemy jets

    canvas.create_rectangle(x0-10, y0-10, x0+10, y0+40, outline = 'black',
                            fill = 'DarkSlateGray4')

    # draw jet's missile shooter

    canvas.create_rectangle(x0-8, y0+40, x0+8, y0+45, outline = 'medium violet red', 
                            fill = 'medium violet red')
    
    #draw right wing 
    
    canvas.create_polygon(x0-10, y0, x0-50, y0, x0-30, y0+20, x0-10, y0+20, 
                            fill = 'DarkSlateGray4', outline = 'black')
    # draw right tail

    #draw left wing
    canvas.create_polygon(x0+10, y0, x0+50, y0, x0+30, y0+20, x0+10, y0+20, 
                            fill = 'DarkSlateGray4', outline = 'black')
    #draw left tail 

# def drawEnemyJetFractal(app, canvas, level, cx, cy):
#     if level == 0: 
#         drawEnemyJet(app, canvas, cx, cy)
#     else:


def spawnEnemyJet(app):
    if app.pause:
        return
    enemySpawnX0 = random.randint(60, app.width-110)
    app.enemySpawnX0 = enemySpawnX0
    bound1 = app.enemySpawnX0 - 60
    bound2 = app.enemySpawnX0 + 110
    if len(app.enemyJets) <= 4:
        if isNotOverlap(app, bound1, bound2):
            app.enemyJetXCoord.add(app.enemySpawnX0)
            app.enemyJets.append([app.enemySpawnX0, app.enemySpawnY0])

def isNotOverlap(app, bound1, bound2):
    include = set(range(bound1, bound2+1))
    for num in include:
        if num in app.enemyJetXCoord:
            return False
    return True
 

def moveEnemyJet(app):
    if app.pause:
        return
    else:
        # x-coordinate --> coordinate[0]
        # y-coordinate --> coordinate[1]
        for coordinate in app.enemyJets:
            coordinate[1] += 1
            if hitBoxEnemy(app, coordinate):
                app.enemyJets.remove(coordinate)
                app.enemyJetXCoord.remove(coordinate[0])
                app.score += 1
            if coordinate[1] >= app.height-100:
                app.enemyJets.remove(coordinate)
                app.enemyJetXCoord.remove(coordinate[0])

def drawEnemyMissile(app, canvas, x, y):
    canvas.create_polygon(x-8, y+45, x+8, y+45, x, y+50, fill = 'purple',
                            outline = 'red')

def addEnemyMissile(app):
    for x, y in app.enemyJets:
        missileType = random.choice(app.enemyMissileTypes)
        if missileType == 'linear':
            missile = classes.Linear(x, y)
        elif missileType == 'sin':
            missile = classes.Sinusoidal(x, y)
        elif missileType == 'para1':
            missile = classes.Parabolic(x, y)
        elif missileType == 'para2':
            missile = classes.Parabolic2(x, y)
        app.enemyMissiles.append([missile, x, y])

def shootEnemyMissile(app):
    for info in app.enemyMissiles:
        dy = info[0].eq()[0]
        dx = info[0].eq()[1]
        info[2] += dy
        info[1] += dx
        if hitBoxUser(app):
            app.health -= 1
            if app.health <= 0:
                app.gameOver = True
        elif info[2] >= app.height:
            app.enemyMissiles.remove(info)
    

def shootUserMissile(app):
    for pair in app.userMissiles:
        pair[1] -= 10
        if pair[1] <= -700:
            app.userMissiles.remove(pair)
            app.MissilesInAir -= 2

# hitbox when enemy missiles hit user's jet
def hitBoxUser(app):
    for coords in app.enemyMissiles:
        x = coords[1]
        y = coords[2]
        possibleX = [x-8, x+8, x]
        for x in possibleX:
            if app.UserX-80 <= x <= app.UserX+80:
                if y >= app.UserY-40:
                    app.enemyMissiles.remove(coords)
                    return True
    
    return False

# hitbox when user missiles hit enemy's jet
def hitBoxEnemy(app, coordPair):
    for coords in app.userMissiles:
        x = coords[0]
        y = coords[1]
        wingY = (y-10+app.height-30)//2
        possibleX = [x-27.5, x+27.5, x-37.5, x+37.5]
        for x in possibleX:
            if coordPair[0]-50 <= x <= coordPair[0]+50:
                if coordPair[1] <= wingY <= coordPair[1] + 50:
                    app.userMissiles.remove(coords)
                    app.MissilesInAir -= 2
                    return True
    
    return False

def redrawAll(app, canvas):
    # draw background first
    drawBackground(app, canvas)
    # draw user's jet
    drawUserJet(app, canvas, app.UserX, app.UserY)
    # draw missiles shot by user
    for x,y in app.userMissiles:
        drawUserMissiles(app, canvas, x, y)
    # draw enemy jets 
    for coordinate in app.enemyJets:
        drawEnemyJet(app, canvas, coordinate[0], coordinate[1])
    # draw enemy missiles
    for coordinate in app.enemyMissiles:
        drawEnemyMissile(app, canvas, coordinate[1], coordinate[2])
    
    # extra features/gameplay information
    # draw health bar
    drawHealthBar(app, canvas, app.health)
    # draw box to enclosed missile counter and score
    cx = app.width//2
    cy = 50
    canvas.create_rectangle(cx -210, cy-30, cx + 210, cy + 60, fill = 'black')
    # draw missiles in the air 
    drawMissileCounter(app, canvas)
    # draw score (enemy jets taken down)
    drawScore(app, canvas)
    
    # game over animation (condition 1)
    if app.MissilesInAir > 50:
        cx = app.width//2
        cy = app.height//2
        canvas.create_rectangle(cx - 310, cy - 50, cx + 310, cy + 60, fill = 'black')
        canvas.create_text(app.width//2, app.height//2, 
                            text = 'System Failure: Overheat'.upper(), fill = 'red',
                            font = 'Courier 40 bold')
        canvas.create_text(app.width//2, app.height//2+30, text = "[Missile Limit: 50] (EXCEEDED)", fill = 'red',
                            font = 'Courier 20 bold')
    elif app.MissilesInAir >= 40:
        canvas.create_text(app.width//2, app.height//2, 
                            text = 'Overheating: Missiles Fired Exceeding Limit', fill = 'orange',
                            font = 'Courier 40 bold')
    # game over animation (condition 2)
    if app.health <= 0:
        cx = app.width // 2
        cy = app.height//2
        canvas.create_rectangle(cx-200, cy-100, cx+200, cy+100, fill = 'black')
        canvas.create_text(app.width//2, app.height//2-20, text = 'FIGHTER DOWN', 
                            fill = 'red', font = 'Courier 40 bold')
        canvas.create_text(app.width//2, app.height//2+50, 
                            text = 'Press "r" to restart', fill = 'red', 
                            font = 'Courier 30 bold')
    elif app.health <= 20:
        if app.timePassed % 50 == 0:
            canvas.create_text(1150, 100, text = "WARNING", fill= 'red',
                                font = 'Courier 90 bold')
    
    # draw pause button/pause animation
    drawPauseButton(app, canvas)
    if app.pause:
        drawPause(app, canvas)
    if app.gameOver:
        canvas.create_text(app.width//2, 10, text = "Game Over", fill = 'black', 
                            font = 'Courier 15 bold')
    
# change width to 1440 (final)
runApp(width = 1440, height = 778)



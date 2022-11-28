from cmu_112_graphics import *
import jetC
import mslC
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
    app.difficultyTracker = 0
    app.enemyJetCapacity = 0
    app.timerDelay = 10
    app.pause = False
    app.mslPerSec = 2000 # increase fire rate by 0.04s every 10 targets down

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
    app.specialActivated = False
    app.MissilesInAir = 0
    app.userMissiles = []
    # app.image1 = 

    # selection of Jets (for user)
    Hawk = jetC.Hawk(300, 100, app.UserX, app.UserY)
    Falcon = jetC.Falcon(400, 75, app.UserX, app.UserY)
    Thunderbolt = jetC.Thunderbolt(250, 150, app.UserX, app.UserY)
    app.jetSelection = [Hawk, Falcon, Thunderbolt]
    app.userJet = random.choice(app.jetSelection)
    app.userJetFull = app.userJet.health

    # types of missiles (for enemy)
    # app.enemyMissileTypes = ['cubic']
    app.enemyMissileTypes = ['linear', 'sin', 'para1', 'para2', 'cubic']


def mousePressed(app, event):
    if app.gameOver:
        return
    if app.pause:
        if app.width//2-110 <= event.x <= app.width//2+110:
            if app.height//2-50 <= event.y <= app.height//2+60:
                app.pause = False
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
        if app.userJet.UserX+50 >= app.width:
            app.userJet.UserX = 50
        else: 
            app.userJet.UserX += app.userJet.speed
    # move user jet to the left
    if event.key == 'Left' or event.key == 'a':
        if app.userJet.UserX-50 <= 0:
            app.userJet.UserX = app.width-50
        else: 
            app.userJet.UserX -= app.userJet.speed
    # shoot missiles from user jet
    if event.key == 't':
        app.specialActivated = not app.specialActivated

    if event.key == 'Space':
        if app.specialActivated:
            getUserMissileCoord(app)
        else:
            getUserMissileCoord(app)
        if app.MissilesInAir > 30:
            app.gameOver = not app.gameOver
            app.userJet.health = 0
        

def timerFired(app):
    if app.gameOver:
        return
    if app.pause:
        return
    app.timePassed += app.timerDelay
    app.difficultyTracker += app.timerDelay
    if app.difficultyTracker == 30000:
        app.difficultyTracker = 0
        app.enemyJetCapacity += 1
    
    # if game is not paused or over
    if app.timePassed % 100 == 0:
        spawnEnemyJet(app)
    if app.timePassed % 5 == 0:
        moveEnemyJet(app)
    # need to set general variable for addEnemyMissile (default = 1000)
    if app.timePassed % app.mslPerSec == 0:
    # if app.timePassed % 200 == 0: # test conditional
        addEnemyMissile(app)
    # need to set general variable for shootEnemyMissile
    if app.timePassed % 10 == 0:
        shootEnemyMissile(app)
        shootUserMissile(app)

def drawHealthBar(app, canvas, health, divider):
    x0 = 0
    x1 = 1/10 * app.width
    y0 = 0
    y1 = 1/50 * app.height
    # draw rectangle to fill in colors when health bars disappear
    canvas.create_rectangle(x0, y0, app.width, y1, fill = 'dark gray')
    for bar in range(health//divider):
        canvas.create_rectangle(x0, y0, x1, y1, fill = 'red', 
                                    outline = 'white', width = 3)
        x0, x1 = x1, (x1 + 1/10*app.width)
    x0 = 0
    x1 = app.width
    y0 = 1/50 * app.height
    y1 = 1/50 * app.height
    canvas.create_line(x0, y0, x1, y1, fill = 'tan')
    # draw heart icon
    cx = app.width-100
    cy = 160
    canvas.create_rectangle(cx-15, cy-135, cx+15, 
                            cy-105, fill = 'snow')
    canvas.create_rectangle(cx-13, cy-125, cx+13, 
                            cy-115, fill = 'red', outline = 'red')
    canvas.create_rectangle(cx-5, cy-132, cx+5, 
                            cy-108, fill = 'red', outline = 'red')
    # draw health number 
    canvas.create_text(app.width-45, 42, text = f'{app.userJet.health}',
                        fill = 'red', font = 'Courier 30 bold')


def drawPauseButton(app, canvas):
    canvas.create_image
    canvas.create_rectangle(25, 25, 50, 50, fill = 'navy blue', outline = 'royal blue',
                            width = 3)
    canvas.create_text(40, 60, text = 'Pause/Resume', font = 'Courier 10 bold',
                        fill = 'white')
    
def drawPause(app, canvas):
    cx = app.width//2
    cy = app.height//2
    canvas.create_rectangle(cx - 110, cy - 50, cx + 110, cy + 60, fill = 'black')
    canvas.create_text(app.width//2, app.height//2, text = 'Game paused', 
                        font = 'Courier 30 bold', fill = 'red')
    canvas.create_text(app.width//2, app.height//2+25, text = 'Press "p" to unpause', fill = 'red',
                        font = 'Courier 15 bold')

def drawScore(app, canvas):
    canvas.create_text(app.width//2, 40, text = f"Targets Down: {app.score}", 
                        fill = 'green', font = 'Courier 30 bold')

def drawBackground(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'black')

def getUserMissileCoord(app):
    if app.specialActivated:
        special = mslC.Special(app.userJet.UserX, app.userJet.UserY)
        app.userMissiles.append(special)
    else:
        linear = mslC.ULinear(app.userJet.UserX, app.userJet.UserY)
        app.userMissiles.append(linear)
    # each actual missile x-coordinate in userMissile is +- 7.5 units from
    # the x-coordinate in the userMissiles list
    app.MissilesInAir += 2
    

def drawMissileCounter(app, canvas):
    canvas.create_text(app.width//2, 68, text = f'Missiles On Course: {app.MissilesInAir}', 
                        fill = "green", font = 'Courier 20')
    canvas.create_text(app.width//2, 90, text = f'Enemy Fire Rate: 1 msls/{app.mslPerSec/1000}sec', fill = 'green',
                        font = 'Courier 15')

def drawEnemyJet(app, canvas, x0, y0, unit):
    # draw jet's body
    # x and y-coord in app.enemyJets are the center coordinates of enemy jets

    canvas.create_rectangle(x0-10*unit, y0-10*unit, x0+10*unit, y0+40*unit, outline = 'black',
                            fill = 'silver')

    # draw jet's missile shooter

    canvas.create_arc(x0-8*unit, y0+35*unit, x0+8*unit, y0+50*unit, outline = 'black', 
                            fill = 'medium violet red', extent = -180)
    
    #draw right wing 
    
    canvas.create_polygon(x0-10*unit, y0, x0-50*unit, y0, x0-30*unit, 
                        y0+20*unit, x0-10*unit, y0+20*unit, 
                        fill = 'SlateGray2', outline = 'black')
    # draw right tail

    #draw left wing
    canvas.create_polygon(x0+10*unit, y0, x0+50*unit, y0, x0+30*unit, 
                            y0+20*unit, x0+10*unit, y0+20*unit, 
                            fill = 'SlateGray2', outline = 'black')
    #draw left tail 


# draw enemy jet fractal (if have time)


# spawns enemy jets at the top of the screen
def spawnEnemyJet(app):
    if app.pause:
        return
    enemySpawnX0 = random.randint(60, app.width-110)
    app.enemySpawnX0 = enemySpawnX0
    bound1 = app.enemySpawnX0 - 60
    bound2 = app.enemySpawnX0 + 110
    if len(app.enemyJets) <= app.enemyJetCapacity:
        if isNotOverlap(app, bound1, bound2):
            app.enemyJetXCoord.add(app.enemySpawnX0)
            app.enemyJets.append([app.enemySpawnX0, app.enemySpawnY0])

# makes sure enemy jets don't overlap when spawning into the window
def isNotOverlap(app, bound1, bound2):
    include = set(range(bound1, bound2+1))
    for num in include:
        if num in app.enemyJetXCoord:
            return False
    return True
 
# moves enemy jet down the window
def moveEnemyJet(app):
    if app.pause:
        return
    else:
        # x-coordinate --> coordinate[0]
        # y-coordinate --> coordinate[1]
        for coordinate in app.enemyJets:
            coordinate[1] += 2
            if hitBoxEnemy(app, coordinate):
                app.enemyJets.remove(coordinate)
                app.enemyJetXCoord.remove(coordinate[0])
                app.score += 1
                if app.score % 5 == 0:
                    app.mslPerSec -= 25
                    if app.mslPerSec <= 0:
                        app.mslPerSec = 25
                # user gains 5 health when killing enemy jet
                # if app.userJet.health <= app.userJetFull:
                #     app.userJet.health += 2
                #     if app.userJet.health > app.userJetFull:
                #         app.userJet.health = app.userJetFull
            if coordinate[1] >= app.height-100:
                app.enemyJets.remove(coordinate)
                app.enemyJetXCoord.remove(coordinate[0])
                app.userJet.health -= 10

# chooses random missile type and adds it to enemy jet
def addEnemyMissile(app):
    for x, y in app.enemyJets:
        missileType = random.choice(app.enemyMissileTypes)
        if missileType == 'linear':
            missile = mslC.Linear(x, y)
        elif missileType == 'sin':
            missile = mslC.Sinusoidal(x, y)
        elif missileType == 'para1':
            missile = mslC.Parabolic(x, y)
        elif missileType == 'para2':
            missile = mslC.Parabolic2(x, y)
        elif missileType == 'cubic':
            missile  = mslC.Cubic(x, y)
        app.enemyMissiles.append(missile)

# shoots enemy missile from enemy missile list 
def shootEnemyMissile(app):
    for missile in app.enemyMissiles:
        missile.eq()
        if hitboxUserEnemyMissiles(app, app.userMissiles, missile):
            app.enemyMissiles.remove(missile)
            app.userMissiles.remove(app.userMissiles[0])
            app.MissilesInAir -= 2
        elif hitBoxUser(app):
            app.userJet.health -= missile.damage
            if app.userJet.health <= 0:
                app.gameOver = True
        elif missile.y >= app.height:
            app.enemyMissiles.remove(missile)
        
    
# shoots missile when user presses 'space'
def shootUserMissile(app):
    for missile in app.userMissiles:
        missile.eq()
        if missile.y <= -700:
            app.userMissiles.remove(missile)
            app.MissilesInAir -= 2

# hitbox when enemy missiles hit user's jet
def hitBoxUser(app):
    for missile in app.enemyMissiles:
        x = missile.x
        y = missile.y
        possibleX = [x-8, x+8, x]
        for x in possibleX:
            if app.userJet.UserX-80 <= x <= app.userJet.UserX+80:
                if y >= app.userJet.UserY-40 and y <= app.userJet.UserY+40:
                    app.enemyMissiles.remove(missile)
                    return True
    
    return False

# hitbox when user missiles hit enemy's jet
def hitBoxEnemy(app, coordPair):
    for missile in app.userMissiles:
        x = missile.x
        y = missile.y
        wingY = (y-10+app.height-30)//2
        possibleX = [x-27.5, x+27.5, x-37.5, x+37.5]
        for x in possibleX:
            if coordPair[0]-50 <= x <= coordPair[0]+50:
                if coordPair[1] <= wingY <= coordPair[1] + 50:
                    app.userMissiles.remove(missile)
                    app.MissilesInAir -= 2
                    return True
    
    return False

# if user missile hits enemy missile, both missiles cancel out
def hitboxUserEnemyMissiles(app, userMissiles, enemyMissile):
    # compare user missile list with enemy missile list 
    if len(userMissiles) == 0:
        return False
    else:
        x = userMissiles[0].x
        y = userMissiles[0].y
        wingY = (userMissiles[0].y-10+app.height-30)//2
        possibleX = [enemyMissile.x-7.5, enemyMissile.x+7.5]
        for x1 in possibleX:
            if x-37.5 <= x1 <= x+37.5:
                if wingY-12 <= enemyMissile.y <= wingY:
                    return True
        return hitboxUserEnemyMissiles(app, userMissiles[1:], enemyMissile)


def redrawAll(app, canvas):
    # draw background first
    drawBackground(app, canvas)
    # draw icon for enemy jet capacity
    drawEnemyJet(app, canvas, app.width - 95, 73, 0.5)
    # draw user's jet
    app.userJet.redraw(app, canvas)
    # draw missiles shot by user
    for missile in app.userMissiles:
        missile.redraw(app, canvas)
    # draw enemy jets 
    for coordinate in app.enemyJets:
        drawEnemyJet(app, canvas, coordinate[0], coordinate[1], 1)
    # draw enemy missiles
    for missile in app.enemyMissiles:
        missile.redraw(app, canvas)
    # extra features/gameplay information
    # draw health bar
    drawHealthBar(app, canvas, app.userJet.health, app.userJetFull//10)
    # draw box to enclosed missile counter and score
    cx = app.width//2
    cy = 50
    canvas.create_rectangle(cx -210, cy-30, cx + 210, cy + 60, fill = 'black')
    # draw missiles in the air 
    drawMissileCounter(app, canvas)
    # draw score (enemy jets taken down)
    drawScore(app, canvas)
    
    # game over animation (condition 1)
    if app.MissilesInAir > 30:
        cx = app.width//2
        cy = app.height//2
        canvas.create_rectangle(cx - 310, cy - 50, cx + 310, cy + 60, fill = 'black')
        canvas.create_text(app.width//2, app.height//2, 
                            text = 'System Failure: Overheat'.upper(), fill = 'red',
                            font = 'Courier 40 bold')
        canvas.create_text(app.width//2, app.height//2+30, text = "[Missile Limit: 30] (EXCEEDED)", fill = 'red',
                            font = 'Courier 20 bold')
    elif app.MissilesInAir >= 20:
        canvas.create_text(app.width//2, app.height//2, 
                            text = 'Overheating: Missiles Fired Exceeding Limit', fill = 'orange',
                            font = 'Courier 40 bold')
    # game over animation (condition 2)
    elif app.userJet.health <= 0:
        cx = app.width // 2
        cy = app.height//2
        canvas.create_rectangle(cx-200, cy-100, cx+200, cy+100, fill = 'black')
        canvas.create_text(app.width//2, app.height//2-20, text = 'FIGHTER DOWN', 
                            fill = 'red', font = 'Courier 40 bold')
        canvas.create_text(app.width//2, app.height//2+50, 
                            text = 'Press "r" to restart', fill = 'red', 
                            font = 'Courier 30 bold')
    elif app.userJet.health <= 20:
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

    # show enemy jet capacity
    canvas.create_text(app.width-50, 80, text = f"{app.enemyJetCapacity+1}", fill= 'red',
                                font = 'Courier 30 bold')
    
# change width to 1440 (final)
runApp(width = 1440, height = 778)



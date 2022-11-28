import math

# missile class (different types of missiles that enemy jets can shoot)
    
class Linear:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 10
        # time passed for each missile movement (lower the number, the faster the speed)
        self.speed = 15

    def eq(self):
        # if self.y == 350:
        #     self.y = 0
        # else:
        self.y += self.speed
        

    def redraw(self, app, canvas):
        canvas.create_oval(self.x-8, self.y+45, self.x+8, self.y+55, fill = 'purple',
                            outline = 'red')

class Sinusoidal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 5
        # time passed for each missile movement (lower the number, the faster the speed)
        self.speed = 5

    def eq(self):
        # if self.y == 350:
        #     self.y = 0
        # else:
        self.y += self.speed
        self.x += 10*math.sin(10*self.y)
        

    def redraw(self, app, canvas):
        canvas.create_arc(self.x-5, self.y+45, self.x+5, self.y+75, 
                            fill = 'blue', outline = 'teal', width = 2,
                            extent = -180)

class Parabolic:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 1
        # time passed for each missile movement (lower the number, the faster the speed)
        self.speed = 10
    
    def eq(self):
        # if self.y == 350:
        #     self.y = 0
        # else:
        self.y += self.speed
        self.x += 0.00005*(self.y**2)
        

    def redraw(self, app, canvas):
        canvas.create_polygon(self.x-5, self.y+45, self.x+5, self.y+45, self.x, 
                                self.y+50, fill = 'OrangeRed',
                            outline = 'red', width = 2)
        canvas.create_polygon(self.x-5, self.y+45, self.x+5, self.y+45, self.x, 
                                self.y+40, fill = 'OrangeRed',
                            outline = 'red', width = 2)


class Parabolic2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 1
        # time passed for each missile movement (lower the number, the faster the speed)
        self.speed = 10
    
    def eq(self):
        # if self.y == 350:
        #     self.y = 0
        # else:
        self.y += self.speed
        self.x += -0.00005*(self.y**2)
        

    def redraw(self, app, canvas):
        canvas.create_polygon(self.x-5, self.y+45, self.x+5, self.y+45, self.x, 
                                self.y+50, fill = 'OrangeRed',
                            outline = 'red', width = 2)
        canvas.create_polygon(self.x-5, self.y+45, self.x+5, self.y+45, self.x, 
                                self.y+40, fill = 'OrangeRed',
                            outline = 'red', width = 2)

class Cubic:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 2
        # time passed for each missile movement (lower the number, the faster the speed)
        self.speed = 5
    
    def eq(self):
        self.y += self.speed
        self.x += 0.00000005*self.y**3-5

    def redraw(self, app, canvas):
        canvas.create_polygon(self.x-15, self.y+45, self.x+15, self.y+45, self.x, 
                                self.y+53, fill = 'green',
                            outline = 'pale green', width = 2)

# special power for user
class Special:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 10
        # time passed for each missile movement (lower the number, the faster the speed)
        self.speed = 20
    
    def eq(self):
        if self.y == 350:
            self.y = 0
        else:
            self.y -= 10
            self.x += 10*math.cos(5*self.y)

    def redraw(self, app, canvas):
        wingY = (self.y-10+app.height-30)//2
        # right missile
        mslCx = self.x + 7.5
        # canvas.create_rectangle(mslCx - 2, wingY + 35, mslCx + 2, wingY + 40, outline = 'green')
        canvas.create_oval(mslCx + 30, wingY - 12, mslCx + 20, wingY, 
                                fill = 'DarkSlateGray', outline = 'misty rose')

        # left missile
        mslCx1 = self.x - 7.5
        canvas.create_oval(mslCx1 - 30, wingY - 12, mslCx1 - 20, wingY, 
                                fill = 'DarkSlateGray1', outline = 'misty rose')


class ULinear:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 10
        # time passed for each missile movement (lower the number, the faster the speed)
        self.speed = 15

    def eq(self):
        # if self.y == 350:
        #     self.y = 0
        # else:
        self.y -= self.speed
        

    def redraw(self, app, canvas):
        wingY = (self.y-10+app.height-30)//2
        # right missile
        mslCx = self.x + 7.5
        # canvas.create_rectangle(mslCx - 2, wingY + 35, mslCx + 2, wingY + 40, outline = 'green')
        canvas.create_rectangle(mslCx + 30, wingY - 10, mslCx + 20, wingY, 
                                fill = 'DarkSlateGray1', outline = 'misty rose')

        # left missile
        mslCx1 = self.x - 7.5
        canvas.create_rectangle(mslCx1 - 30, wingY - 10, mslCx1 - 20, wingY, 
                                fill = 'DarkSlateGray1', outline = 'misty rose')

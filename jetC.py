import math
from cmu_112_graphics import * 

# user jet class (selection of jets player can choose from)
class Jet:
    def __init__(self, health, speed, UserX, UserY):
        self.health = health
        self.speed = speed
        self.UserX = UserX
        self.UserY = UserY

class Hawk(Jet):
    def __init__(self, health, speed, UserX, UserY):
        super().__init__(health, speed, UserX, UserY)
    def __repr__(self):
        return "Hawk"
    def redraw(self, app, canvas):
        # upper half of body
        canvas.create_arc(self.UserX - 15, self.UserY-10, self.UserX + 15, app.height-30, 
                            fill = 'medium sea green', outline = 'black', 
                            
                            extent = 180)
        # lower half of body
        canvas.create_arc(self.UserX - 15, self.UserY-10, self.UserX + 15, app.height-20, 
                                fill = 'OliveDrab4', outline = 'black',
                                
                                extent = -180)
        # pilot's head-up-display (HUD)
        canvas.create_oval(self.UserX - 7, self.UserY-5, self.UserX + 7, app.height-80, fill = 'LightSteelBlue4',
                                outline = 'black')
        # right front wing
        wingY = (self.UserY-10+app.height-30)//2     
        canvas.create_polygon(self.UserX + 15, wingY, self.UserX + 50, wingY, self.UserX + 80, wingY + 20, 
                                self.UserX + 10, wingY + 20, outline = 'black', fill = 'OliveDrab4')

        # right tail
        canvas.create_polygon(self.UserX + 10, wingY + 40, self.UserX + 30, wingY + 40, self.UserX + 50, wingY + 55, 
                                self.UserX + 5, wingY + 55, outline = 'black', fill = 'gray16')

        # left front wing
        canvas.create_polygon(self.UserX - 15, wingY, self.UserX - 50, wingY, self.UserX - 80, wingY + 20, 
                                self.UserX - 10, wingY + 20, outline = 'black', fill = 'gray16')

        # left tail
        canvas.create_polygon(self.UserX - 10, wingY + 40, self.UserX - 30, wingY + 40, self.UserX - 50, wingY + 55, 
                                self.UserX - 5, wingY + 55, outline = 'black', fill = 'OliveDrab4')

        # right missile shooter
        mslCx = self.UserX + 7.5
        # canvas.create_rectangle(mslself.UserX - 2, wingY + 35, mslself.UserX + 2, wingY + 40, outline = 'green')
        canvas.create_rectangle(mslCx + 30, wingY - 10, mslCx + 20, wingY, fill = 'pale goldenrod', outline = 'black')

        # left missile shooter
        mslCx1 = self.UserX - 7.5
        canvas.create_rectangle(mslCx1 - 30, wingY - 10, mslCx1 - 20, wingY, fill = 'pale goldenrod', outline = 'black')

        # name tag
        canvas.create_text(self.UserX, self.UserY+140, text = self, fill = 'white',
                            font = 'Courier 10 bold')


class Falcon(Jet):
    def __init__(self, health, speed, UserX, UserY):
        super().__init__(health, speed, UserX, UserY)
    def __repr__(self):
        return "Falcon"
    def redraw(self, app, canvas):
        # upper half of body
        canvas.create_arc(self.UserX - 15, self.UserY-10, self.UserX + 15, app.height-30, 
                            fill = 'bisque4', outline = 'black', 
                            
                            extent = 180)
        # lower half of body
        canvas.create_arc(self.UserX - 15, self.UserY-10, self.UserX + 15, app.height-20, 
                                fill = 'bisque4', outline = 'black',
                                
                                extent = -180)
        # pilot's head-up-display (HUD)
        canvas.create_oval(self.UserX - 7, self.UserY-5, self.UserX + 7, app.height-80, fill = 'GreenYellow',
                                outline = 'green', width = 2)
        # right front wing
        wingY = (self.UserY-10+app.height-30)//2     
        canvas.create_polygon(self.UserX + 15, wingY, self.UserX + 50, wingY, self.UserX + 80, wingY + 20, 
                                self.UserX + 10, wingY + 20, outline = 'black', fill = 'burlywood4')

        # right tail
        canvas.create_polygon(self.UserX + 10, wingY + 40, self.UserX + 30, wingY + 40, self.UserX + 50, wingY + 55, 
                                self.UserX + 5, wingY + 55, outline = 'black', fill = 'burlywood4')

        # left front wing
        canvas.create_polygon(self.UserX - 15, wingY, self.UserX - 50, wingY, self.UserX - 80, wingY + 20, 
                                self.UserX - 10, wingY + 20, outline = 'black', fill = 'burlywood4')

        # left tail
        canvas.create_polygon(self.UserX - 10, wingY + 40, self.UserX - 30, wingY + 40, self.UserX - 50, wingY + 55, 
                                self.UserX - 5, wingY + 55, outline = 'black', fill = 'burlywood4')

        # right missile shooter
        mslCx = self.UserX + 7.5
        # canvas.create_rectangle(mslself.UserX - 2, wingY + 35, mslself.UserX + 2, wingY + 40, outline = 'green')
        canvas.create_rectangle(mslCx + 30, wingY - 10, mslCx + 20, wingY, fill = 'coral4', outline = 'black')

        # left missile shooter
        mslCx1 = self.UserX - 7.5
        canvas.create_rectangle(mslCx1 - 30, wingY - 10, mslCx1 - 20, wingY, fill = 'coral4', outline = 'black')
    
        # name tag
        canvas.create_text(self.UserX, self.UserY+140, text = self, fill = 'white',
                            font = 'Courier 10 bold')

class Thunderbolt(Jet):
    def __init__(self, health, speed, UserX, UserY):
        super().__init__(health, speed, UserX, UserY)
    def __repr__(self):
        return "Thunderbolt"
    def redraw(self, app, canvas):
        # upper half of body
        canvas.create_arc(self.UserX - 15, self.UserY-10, self.UserX + 15, app.height-30, 
                            fill = 'grey61', outline = 'black', 
                            
                            extent = 180)
        # lower half of body
        canvas.create_arc(self.UserX - 15, self.UserY-10, self.UserX + 15, app.height-20, 
                                fill = 'grey30', outline = 'black',
                                
                                extent = -180)
        # pilot's head-up-display (HUD)
        canvas.create_oval(self.UserX - 7, self.UserY-5, self.UserX + 7, app.height-80, fill = 'medium slate blue',
                                outline = 'purple')
        # right front wing
        wingY = (self.UserY-10+app.height-30)//2     
        canvas.create_polygon(self.UserX + 15, wingY, self.UserX + 50, wingY, self.UserX + 80, wingY + 20, 
                                self.UserX + 10, wingY + 20, outline = 'black', fill = 'grey35')

        # right tail
        canvas.create_polygon(self.UserX + 10, wingY + 40, self.UserX + 30, wingY + 40, self.UserX + 50, wingY + 55, 
                                self.UserX + 5, wingY + 55, outline = 'black', fill = 'grey35')

        # left front wing
        canvas.create_polygon(self.UserX - 15, wingY, self.UserX - 50, wingY, self.UserX - 80, wingY + 20, 
                                self.UserX - 10, wingY + 20, outline = 'black', fill = 'grey35')

        # left tail
        canvas.create_polygon(self.UserX - 10, wingY + 40, self.UserX - 30, wingY + 40, self.UserX - 50, wingY + 55, 
                                self.UserX - 5, wingY + 55, outline = 'black', fill = 'grey35')

        # right missile shooter
        mslCx = self.UserX + 7.5
        # canvas.create_rectangle(mslself.UserX - 2, wingY + 35, mslself.UserX + 2, wingY + 40, outline = 'green')
        canvas.create_rectangle(mslCx + 30, wingY - 10, mslCx + 20, wingY, fill = 'MediumPurple4', outline = 'black')

        # left missile shooter
        mslCx1 = self.UserX - 7.5
        canvas.create_rectangle(mslCx1 - 30, wingY - 10, mslCx1 - 20, wingY, fill = 'MediumPurple4', outline = 'black')

        # name tag
        canvas.create_text(self.UserX, self.UserY+140, text = self, fill = 'white',
                            font = 'Courier 10 bold')


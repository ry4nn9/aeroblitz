class Squadron:
    def __init__(self): 
        self.team = []
    def addJet(self, jet):
        self.team.append(jet)
    def redraw(self, app, canvas):
        for jet in self.team:
            jet.redraw(app, canvas)

class Enemy(Squadron):
    def __init__(self, health, speed, EnemyX, EnemyY):
        self.health = health
        self.speed = speed
        self.EnemyX = EnemyX
        self.EnemyY = EnemyY
        

class Bomber(Enemy):
    def __init__(self, health, speed, EnemyX, EnemyY):
        super().__init__(health, speed, EnemyX, EnemyY)
        self.fullHealth = self.health
    def redraw(self, app, canvas):
        # draw health bar
        x0 = self.EnemyX-32
        x1 = x0 + 2.5
        y0 = self.EnemyY-20
        y1 = self.EnemyY-15
        canvas.create_rectangle(self.EnemyX-32, y0, self.EnemyX+32, y1, 
                                fill = 'black', outline = 'tan')
        for bar in range(self.health):
            canvas.create_rectangle(x0, y0, x1, y1, fill = 'red', outline = 'red')
            x0, x1 = x1, x0+2.5
        
        # draw jet's body
        # x and y-coord in app.enemyJets are the center coordinates of enemy jets
        canvas.create_rectangle(self.EnemyX-10, self.EnemyY-10, self.EnemyX+10, 
                                self.EnemyY+40, outline = 'black', fill = 'gray64')
        # draw jet's missile shooter
        canvas.create_arc(self.EnemyX-8, self.EnemyY+35, self.EnemyX+8, 
                        self.EnemyY+50, outline = 'black', fill = 'orange', 
                        extent = -180) 
        #draw right wing 
        canvas.create_polygon(self.EnemyX-10, self.EnemyY, self.EnemyX-50, 
                            self.EnemyY, self.EnemyX-30, self.EnemyY+20, 
                            self.EnemyX-10, self.EnemyY+20, 
                            fill = 'SlateGray4', outline = 'black')
        # draw right tail
        #draw left wing
        canvas.create_polygon(self.EnemyX+10, self.EnemyY, self.EnemyX+50, 
                            self.EnemyY, self.EnemyX+30, self.EnemyY+20, 
                            self.EnemyX+10, self.EnemyY+20, 
                            fill = 'SlateGray4', outline = 'black')
        #draw left tail 


class LightFighter(Enemy):
    def __init__(self, health, speed, EnemyX, EnemyY):
        super().__init__(health, speed, EnemyX, EnemyY)
        self.fullHealth = self.health
    def redraw(self, app, canvas):
        # draw health bar
        x0 = self.EnemyX-16
        x1 = x0 + 3
        y0 = self.EnemyY-20
        y1 = self.EnemyY-15
        canvas.create_rectangle(self.EnemyX-16, y0, self.EnemyX+15, y1, 
                                fill = 'black', outline = 'tan')
        for bar in range(self.health):
            canvas.create_rectangle(x0, y0, x1, y1, fill = 'red', outline = 'red')
            x0, x1 = x1, x0+3
        # draw jet's body
        # x and y-coord in app.enemyJets are the center coordinates of enemy jets
        canvas.create_rectangle(self.EnemyX-10, self.EnemyY-10, self.EnemyX+10, 
                                self.EnemyY+40, outline = 'black', fill = 'silver')
        # draw jet's missile shooter
        canvas.create_arc(self.EnemyX-8, self.EnemyY+35, self.EnemyX+8, 
                        self.EnemyY+50, outline = 'black', fill = 'medium violet red', 
                        extent = -180) 
        # draw right wing 
        canvas.create_polygon(self.EnemyX-10, self.EnemyY, self.EnemyX-50, 
                            self.EnemyY, self.EnemyX-30, self.EnemyY+20, 
                            self.EnemyX-10, self.EnemyY+20, 
                            fill = 'SlateGray2', outline = 'black')
        # draw right tail
        # draw left wing
        canvas.create_polygon(self.EnemyX+10, self.EnemyY, self.EnemyX+50, 
                            self.EnemyY, self.EnemyX+30, self.EnemyY+20, 
                            self.EnemyX+10, self.EnemyY+20, 
                            fill = 'SlateGray2', outline = 'black')
        # draw left tail 
        

class Torpedo(Enemy):
    def __init__(self, health, speed, EnemyX, EnemyY):
        super().__init__(health, speed, EnemyX, EnemyY)
        self.fullHealth = self.health
    def redraw(self, app, canvas):
        # draw health bar
        x0 = self.EnemyX-24
        x1 = x0 + 3
        y0 = self.EnemyY-20
        y1 = self.EnemyY-15
        canvas.create_rectangle(self.EnemyX-24, y0, self.EnemyX+22, y1, 
                                fill = 'black', outline = 'tan')
        for bar in range(self.health):
            canvas.create_rectangle(x0, y0, x1, y1, fill = 'red', outline = 'red')
            x0, x1 = x1, x0+3
        # draw jet's body
        # x and y-coord in app.enemyJets are the center coordinates of enemy jets
        canvas.create_rectangle(self.EnemyX-10, self.EnemyY-10, self.EnemyX+10, 
                                self.EnemyY+40, outline = 'black', fill = 'light blue')
        # draw jet's missile shooter
        canvas.create_arc(self.EnemyX-8, self.EnemyY+35, self.EnemyX+8, 
                        self.EnemyY+50, outline = 'black', fill = 'GreenYellow', 
                        extent = -180) 
        # draw right wing 
        canvas.create_polygon(self.EnemyX-10, self.EnemyY, self.EnemyX-50, 
                            self.EnemyY, self.EnemyX-30, self.EnemyY+20, 
                            self.EnemyX-10, self.EnemyY+20, 
                            fill = 'dim grey', outline = 'black')
        # draw right tail
        # draw left wing
        canvas.create_polygon(self.EnemyX+10, self.EnemyY, self.EnemyX+50, 
                            self.EnemyY, self.EnemyX+30, self.EnemyY+20, 
                            self.EnemyX+10, self.EnemyY+20, 
                            fill = 'dim grey', outline = 'black')
        # draw left tail 

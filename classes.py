import math

# user jet class (selection of jets player can choose from)
class Jet:
    def __init__(self, health, speed, missileType, color):
        self.health = health
        self.speed = speed
        self.missileType = missileType
        self.color = color

# missile class (different types of missiles that enemy jets can shoot)
    
class Linear:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # time passed for each missile movement (lower the number, the faster the speed)
        self.speed = 10  

    def eq(self):
        if self.y == 350:
            self.y = 0
        else:
            self.y += 10
        return 10, 0

class Sinusoidal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # time passed for each missile movement (lower the number, the faster the speed)
        self.speed = 30

    def eq(self):
        if self.y == 350:
            self.y = 0
        else:
            self.y += 10
        return 10, 10*math.sin(self.y)

class Parabolic:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # time passed for each missile movement (lower the number, the faster the speed)
        self.speed = 20
    
    def eq(self):
        if self.y == 350:
            self.y = 0
        else:
            self.y += 10
        return 5, 0.000005*(self.y**2)

class Parabolic2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # time passed for each missile movement (lower the number, the faster the speed)
        self.speed = 20
    
    def eq(self):
        if self.y == 350:
            self.y = 0
        else:
            self.y += 10
        return 5, -0.000005*(self.y**2)


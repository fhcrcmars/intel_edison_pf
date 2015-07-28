from Point import Point

class Particle:
    def __init__(self, x=0.0, y=0.0, w=1.0):
        self.location = Point(x,y)
        self.weight = w

    def getLocation(self):
        return str(self.location.getX())+','+str(self.location.getY())

    def getWeight(self):
        return self.weight

    def setLocation(self,x,y):
        self.location.setX(x)
        self.location.setY(y)

    def setWeight(self, w):
        self.weight = w

"""p1= Particle(2,3,5)
print p1.getLocation()
print p1.getWeight()
p1.setLocation(10,11)
p1.setWeight(15)
print p1.getLocation()
print p1.getWeight()
"""

import math

class Point:
    def __init__(self, x=0.0 , y=0.0):
        self.x = x;
        self.y = y;

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y

    def toString(self):
        return '('+str(self.x)+','+str(self.y)+')'
    
    @staticmethod
    def getVector(p1,p2):
        return Point(p2.x-p1.x, p2.y-p1.y)
    
    @staticmethod
    def getDistance(p1,p2):
        return float(math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2))
    @staticmethod
    def dotProduct(p1,p2):
        return p1.x * p2.x + p1.y * p2.y
    @staticmethod
    def crossProduct(p1,p2):
        return p1.x * p2.y - p1.y * p2.x

"""test = Point(2,3)
print test.toString()
test.setX(4)
test.setY(5)
print test.getX()
print test.getY()
test2 = Point()
print test2.toString()
test3 = Point.getVector(test,test2)
print test3.toString()
print Point.getDistance(test,test2)
print Point.dotProduct(test,test2)
print Point.crossProduct(test,test2)
"""

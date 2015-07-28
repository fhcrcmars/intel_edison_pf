from Point import Point

class Line:
    
    def __init__(self, start = Point(), end = Point()):
        self.startPoint = start
        self.endPoint = end

    def getStartPoint(self):
        return self.startPoint

    def getEndPoint(self):
        return self.endPoint
    
    @staticmethod
    def isIntersected(line1, line2):
        vector1 = Point.getVector(line2.startPoint, line1.startPoint)
        vector2 = Point.getVector(line2.startPoint, line1.endPoint)
        vector3 = Point.getVector(line2.startPoint, line2.endPoint)
        if Point.crossProduct(vector1, vector3) * Point.crossProduct(vector2, vector3) > 0:
            return False

        vector1 = Point.getVector(line1.startPoint, line2.startPoint)
        vector2 = Point.getVector(line1.startPoint, line2.endPoint)
        vector3 = Point.getVector(line1.startPoint, line1.endPoint)
        if Point.crossProduct(vector1, vector3) * Point.crossProduct(vector2, vector3) > 0:
            return False

        return True

"""
line1 = Line(Point(0,0),Point(10,10))
line2 = Line(Point(0,10),Point(10,0))
print line1.getStartPoint().toString()
print line1.getEndPoint().toString()
print Line.isIntersected(line1,line2)
"""

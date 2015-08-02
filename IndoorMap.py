from Point import Point
from Line import Line
import math

class IndoorMap:
    
    def __init__(self):
        self.min_x = 100
        self.min_y = 100
        self.max_x = 0
        self.max_y = 0
        self.mapName = 'NTHU_Delta_5F.txt'
        self.inlineList = list()
        self.outlineList = list()
        self.refPoint = Point(0,0)
        self.mapFloorPlanInOrOut = 0
        self.mapScale = 0
        self.mapOffset = 0

    def getScale(self):
        return self.mapScale
    
    def getOffset(self):
        return self.mapOffset

    def getMapName(self):
        return self.mapName

    def getRefPoint(self):
        return self.refPoint

    def getMapFloorPlanInOrOut(self):
        return self.mapFloorPlanInOrOut
    
    def getMaxMinValue(self):
        return [self.min_x,self.min_y,self.max_x,self.max_y]
    
    def read_floor_map(self):
        f = open('./indoorMap/'+self.mapName, 'r')
        for line in f.readlines():
            data = line.replace('\n','').split(',')
            data_num = len(data)
            if data[0] == 'inline' and data_num >=5:
                self.inlineList.append( Line( Point( float(data[1]),float(data[2]) ),Point( float(data[3]),float(data[4])) ) )
                self.min_x = min(self.min_x,float(data[1]),float(data[3]))
                self.max_x = max(self.max_x,float(data[1]),float(data[3]))
                self.min_y = min(self.min_y,float(data[2]),float(data[4]))
                self.max_y = max(self.max_y,float(data[2]),float(data[4]))
            elif data[0] == 'outline' and data_num >=5:
                self.outlineList.append( Line( Point( float(data[1]),float(data[2]) ),Point( float(data[3]),float(data[4])) ) )
                self.min_x = min(self.min_x,float(data[1]),float(data[3]))
                self.max_x = max(self.max_x,float(data[1]),float(data[3]))
                self.min_y = min(self.min_y,float(data[2]),float(data[4]))
                self.max_y = max(self.max_y,float(data[2]),float(data[4]))
            elif data[0] == 'mapInfo' and data_num >=3:
                self.mapScale = float(data[1])
                self.mapOffset = float(data[2])
            elif data[0] == 'floorplanInOrOut' and data_num >=2:
                self.mapFloorPlanInOrOut = int(data[1])
        f.close()
        refPoint = Point(self.min_x + 0.1, self.min_y + 0.1)
        """for i in self.inlineList:
            print i.getStartPoint().toString()
        for i in self.outlineList:
            print i.getStartPoint().toString()
        print self.mapScale
        print self.mapOffset
        """
    
    def numOfIntersectInline(self,point):
        num = 0
        line = Line(self.refPoint, point)
        for wall in self.inlineList:
            if Line.isIntersected(wall, line):
                num += 1
        return num

    def numOfIntersectOutline(self,point):
        num = 0 
        line = Line(self.refPoint, point)
        for wall in self.outlineList:
            if Line.isIntersected(wall, line):
                num += 1
        return num 

"""temp = IndoorMap()
temp.read_floor_map()
for i in temp.getMaxMinValue():
    print i
print temp. numOfIntersectInline(Point(10,10))
print temp. numOfIntersectOutline(Point(10,10))
"""

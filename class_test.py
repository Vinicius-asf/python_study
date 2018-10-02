class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Coord1: " + str(self.x) + " Coord2: " + str(self.y)
    
    def poi(self,name):
        print("oi " + str(name))


class line:
    def __init__(self,x1,y1,x2,y2):
        points = [point(x1,y1),point(x2,y2)]

class square:
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        edges = [line(x1,y1,x2,y2),line(x2,y2,x3,y3),line(x3,y3,x4,y4),line(x4,y4,x1,y1)]


p = point(1,1)
p.poi("Maria")
print(p)
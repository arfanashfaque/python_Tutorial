# class name should strat with a uppercase - Pascals class language
class Point:
    def __init__(self, x, y):   #constuctor   init means initiliaze  and self means reference to the current object
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("Draw")


point = Point(10,20)
print(point.x) #output 10

point.x = 12
print(point.x) #output 12


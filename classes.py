# class name should strat with a uppercase - Pascals class language
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("Draw")


point1 = Point()
point1.x = 10
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 15
print(point2.x)
point2.move()

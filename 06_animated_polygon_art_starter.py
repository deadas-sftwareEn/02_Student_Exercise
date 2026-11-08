import turtle
import random
import math
import time

class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        if pen_size <= 0:
            raise ValueError("Pen size must be positive")
        self._x = x
        self._y = y
        self.sides = sides
        self.side_length = side_length
        self._color = color
        self.angle = angle
        self.pen_size = pen_size
        
        # Setup the turtle
        self._pen = turtle.Turtle()
        self._pen.hideturtle()
        self._pen.speed(0)
        self._pen.color(self._color)
        self._pen.width(self.pen_size)

    def draw(self):
        turn_angle = 360 / self.sides
        for _ in range(self.sides):
            self._pen.forward(self.side_length)
            self._pen.left(turn_angle)

    def move_to(self, x, y):
        self._x = x
        self._y = y
        self._pen.clear()
        self._pen.penup()
        self._pen.goto(self._x, self._y)
        self._pen.setheading(self.angle)
        self._pen.pendown()
        self.draw() 

colors = ["cyan", "turquoise", "orange", "yellowgreen", "deepskyblue",
          "salmon", "plum", "lightgreen", "gold", "pink", "white"]

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(850, 600)
screen.tracer(0)

rng = random.Random(17)
shapes = []
polygons = []  

for _ in range(30):
    sides = rng.randint(3, 6)
    side_length = rng.randint(35, 120)
    x = rng.randint(-350, 260)
    y = rng.randint(-225, 180)
    
    color = rng.choice(colors)
    pen_size = rng.randint(1, 7)
    angle = rng.randint(0, 359)
    
    polygon = Polygon(x, y, sides, side_length, color, pen_size, angle)
    polygon.move_to(x, y)
    polygons.append(polygon)
    
    shapes.append((polygon, x, y, rng.random() * 6.28))

frame = 0
while True:
    for shape, home_x, home_y, phase in shapes:
        x = home_x + 32 * math.cos(frame * 0.11 + phase)
        y = home_y + 23 * math.sin(frame * 0.11 + phase)
        shape.move_to(x, y)  
    screen.update()
    time.sleep(0.045) 
    frame += 1

screen.mainloop()
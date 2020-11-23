from graphics import *
import math


def Circle_draw():
    radius = int(input("Enter the radius of the circle: "))
    pt = Point(250,125)
    cir = Circle(pt, radius)
    win = GraphWin("My Window", 500,500)
    cir.draw(win)
    circumference = 2 * math.pi * radius
    circumference = str(circumference)
    area = math.pi * radius**2
    area = str(area)
    circumference = Text(Point(250,280), "circumference = "+circumference).draw(win)
    area = Text(Point(250,300), "area = "+area).draw(win)

def Rectangle_draw():
    rect = Rectangle(Point(100,100),Point(200,200))
    win = GraphWin("My Window", 500, 500)
    rect.draw(win)
    time.sleep(0.55)
    rect.move(200, 0)

def Circle_double():
    win = GraphWin("My Window", 1000, 1000)
    pt = Point(500,500)
    radius = 1
    while radius > 0:
        cir = Circle(pt, radius)
        radius = radius * 2
        cir.draw(win)
def Shapes():
    count = 0
    while count <= 10:
        shape = input("Pick a shape either a square or a circle or exit: ")
        if shape == "exit":
            count = 10
        elif shape == "square":
            lenght = float(input("Enter the length of the circle: "))
            pt_1 = Point(int(input("Enter the top left point of the circle: ")))
            pt_2 = Point(int(input("Enter the bottom right position of the circle: ")))
            square = Rectange(pt_1,Pt_2)
            win = GraphWin("My Window", 1000, 1000)
            square.draw(win)
            count += 1
        elif shape == "circle":
            radius = float(input("Enter the radius of the circle: "))
            x,y = input("Enter the centre of the circle: ").split(",")
            center = Point(x,y)
            circ = Circle(center, radius)
            win = GraphWin("My Window", 1000, 1000)
            circ.draw(win)
            count += 1
    win.close()
Shapes()
            
            
        
        
    

    

'''
Program: project10p351.txt
Author: Alex Jones
Date: 12/01/21
Purpose: Graphically illustrate a house and
stick figure using Turtle Graphics
'''

from abc import ABC, abstractmethod
from turtle import Turtle

class Shape(ABC):
    
    t = Turtle()
    t.shape("turtle")
    
    def draw(self):
        pass
        
class Line(Shape):
    
    def draw(self, distance, degrees = 0):
        if degrees > 180:
            self.t.right(180-(degrees-180))
        else:
            self.t.left(degrees)
            
        self.t.forward(distance)
        self.t.setheading(0)
        
class Circle(Shape):
    
    def draw(self, radius, extent = 360):
        self.t.circle(radius, extent)
        self.t.setheading(0)
        
class Rectangle(Shape):
    
    def draw(self, height, width, degrees = 0):
        if degrees > 180:
            self.t.right(180-(degrees-180))
        else:
            self.t.left(degrees)
            
            self.t.forward(width)
            self.t.left(90)
            self.t.forward(height)
            self.t.left(90)
            self.t.forward(width)
            self.t.left(90)
            self.t.forward(height)
            self.t.setheading(0)
            
class main():
    
    stick =  Line()
    stickHead = Circle()
    house = Rectangle()
    
    stick.draw(20, 225)
    stick.draw(20, 45)
    stick.draw(20, 315)
    stick.draw(20, 135)
    stick.draw(20, 90)
    stick.draw(20, 45)
    stick.draw(20, 225)
    stick.draw(20, 135)
    stick.draw(20, 315)
    stick.draw(20, 90)

    stickHead.draw(10)
    stickHead.t.up()
    stickHead.t.goto(30, -10)
    stickHead.t.down()
    
    house.draw(100, 150)
    house.t.left(90)
    house.t.forward(100)
    house.t.right(45)
    house.t.forward(106)
    house.t.right(90)
    house.t.forward(106)

    house.t.up()
    house.t.goto(90, -10)
    house.t.down()
    house.t.setheading(0)
    house.draw(75, 30)

    stickHead.t.up()
    stickHead.t.goto(95, 26)
    stickHead.t.down()
    stickHead.t.setheading(0)
    stickHead.draw(3)
    stickHead.t.up()
    stickHead.t.goto(-30, 0)
    
    
if __name__ == "__main__":
    main()

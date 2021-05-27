#Function to draw a spiral in a polygon

import turtle
#Polygon
turtle.pencolor('red')
turtle.hideturtle()
turtle.penup()
turtle.setposition(-44.5,100)
turtle.pendown()

for line in range(8):
    turtle.forward(80)
    turtle.right(45)
    
#Spiral
distance = 0.5
angle = 40
turtle.pencolor('black')
turtle.penup()
turtle.setposition(0,0)
turtle.pendown()
turtle.showturtle()

for turn in range(100):
    turtle.forward(distance)
    turtle.right(angle)
    distance+=0.5

turtle.exitonclick()


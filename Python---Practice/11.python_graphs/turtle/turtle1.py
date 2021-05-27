#Function to draw a rectangle using turtle
#Step by step execution shows pen moving

import turtle

turtle.pencolor('red')  # Set pen color to red, pen seen in center(0,0), faces right, 
turtle.forward(200)     # Move pen forward 200 units (create bottom of rectangle)
turtle.left(90)         # Turn pen to_its_left_by 90 degrees
turtle.pencolor('yellow')
turtle.forward(150)
turtle.left(90)
turtle.pencolor('black')
turtle.forward(200)
turtle.left(90)
turtle.pencolor('blue')
turtle.forward(150)
#turtle.done()          #ends the drawing activity and waits on the user to close the window(no using exitonclick).
turtle.exitonclick()


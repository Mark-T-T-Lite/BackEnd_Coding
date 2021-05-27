#Delay vs speed

import turtle
y = -200 # Initial y value

'''
To use tracer hide all but last update(), hide all delay and speed()(no_need_for_them)
otherwise, unhide all but last update(), unhide all delay and speed()
'''
turtle.tracer(0)
# Default speed and default delay
turtle.color('red')             #   Return or set pencolor and fillcolor
#turtle.pencolor('blue')         #   Return or set pencolor
for x in range(10):
    turtle.penup()
    turtle.setposition(-200, y)
    turtle.pendown()
    turtle.forward(400)
    y += 10
    
# Slowest speed, but no delay
#turtle.speed("slowest")
#turtle.delay(0)
#turtle.update()
turtle.color("blue")
for x in range(10):
    turtle.penup()
    turtle.setposition(-200, y)
    turtle.pendown()
    turtle.forward(400)
    y += 10
    
# Fastest speed with a 500 millisecond delay
#turtle.speed("fastest")
#turtle.delay(500)
#turtle.update()
turtle.color("green")
for x in range(10):
    turtle.penup()
    turtle.setposition(-200, y)
    turtle.pendown()
    turtle.forward(400)
    y += 10
    
# Fastest speed with no delay
#turtle.speed("fastest")
#turtle.delay(0)
#turtle.update()
turtle.color("black")
for x in range(10):
    turtle.penup()
    turtle.setposition(-200, y)
    turtle.pendown()
    turtle.forward(400)
    y += 10

turtle.update()    
turtle.done()


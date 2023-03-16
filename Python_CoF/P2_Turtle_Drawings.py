print("This code uses the Turtle to draw some drawings.\n")

import turtle

turtle.bgcolor("orange")
turtle.pensize(2)

# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)

# turtle.done()

# Drawing a circle.

for i in ['Red','Blue','Green','Yellow','Purple','Cyan']:
    turtle.color(i)
    turtle.circle(150)
    turtle.left(60)
turtle.done()
#	Angkan Biswas
#	07.03.2019
#	Draw a House without any user-defined function

import turtle

#	Draw-rooM
turtle.begin_fill()
turtle.forward(120)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.end_fill()

#	Draw-rooF
turtle.setposition(0,70)
turtle.setheading(0)
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.left(45)
turtle.forward(85)
turtle.right(90)
turtle.forward(85)
turtle.end_fill()

#	Draw-dooR
turtle.penup()
turtle.setposition(20,0)
turtle.setheading(0)
turtle.pendown()
turtle.fillcolor('white')
turtle.begin_fill()
turtle.forward(20)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.end_fill()

#	Draw-windoW
turtle.penup()
turtle.setposition(80,30)
turtle.setheading(0)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.end_fill()
turtle.penup()

turtle.exitonclick()



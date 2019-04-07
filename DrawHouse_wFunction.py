#	Angkan Biswas
#	07.03.2019
#	Draw House with a user defined function

import turtle

#	Define a function to draw a rectangle
def draw_rectangle(x,y,c,w,h):
	turtle.penup()
	turtle.setposition(x,y)
	turtle.setheading(0)
	turtle.pendown()
	turtle.fillcolor(c)
	turtle.begin_fill()
	turtle.forward(w)
	turtle.left(90)
	turtle.forward(h)
	turtle.left(90)
	turtle.forward(w)
	turtle.left(90)
	turtle.forward(h)
	turtle.left(90)
	turtle.end_fill()

#	Call user-defined function to draw a rooM,dooR & windoW
 
draw_rectangle(0,0,'black',120,70)  #	Draw-rooM
draw_rectangle(20,0,'white',20,40)  #	Draw-dooR
draw_rectangle(80,30,'red',20,20)  #	Draw-windoW

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

turtle.exitonclick()



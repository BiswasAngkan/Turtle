#	Angkan Biswas
#	08.03.2019
#	Draw House with three user-defined functions

import turtle

#	Define a user-defined function to draw a rectangle
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

#	Define a user-defined function to draw a trinangle
def draw_triangle(x,y,c):
	turtle.setposition(x,y)
	turtle.setheading(0)
	turtle.fillcolor(c)
	turtle.begin_fill()
	turtle.left(45)
	turtle.forward(85)
	turtle.right(90)
	turtle.forward(85)
	turtle.end_fill()

#	Define a user-defined function to draw a room, door, window & roof of a house
def draw_house(): 
	draw_rectangle(0,0,'black',120,70)   #	Draw-rooM
	draw_rectangle(20,0,'white',20,40)   #	Draw-dooR
	draw_rectangle(80,30,'red',20,20)    #	Draw-windoW
	draw_triangle(0,70,'yellow')	     #	Draw-rooF

#	Call user-defined function to draw a house
draw_house()

turtle.exitonclick()



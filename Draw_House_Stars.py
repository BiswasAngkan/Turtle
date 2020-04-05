#	Angkan Biswas
#	Date-04.04.2020
#	To draw stars & house with user-defined functions

import turtle
from time import sleep

#	Define a function to draw a star

def drawStar(color, x, y):
	turtle.penup()
	turtle.setposition(x, y)
	turtle.pendown()
	turtle.fillcolor(color)


	turtle.begin_fill()
	turtle.forward(3)
	turtle.right(135)
	turtle.forward(3)
	turtle.right(-45)
	turtle.forward(3)
	turtle.right(135)
	turtle.forward(3)
	turtle.left(45)
	turtle.forward(3)
	turtle.right(135)
	turtle.forward(3)
	turtle.left(45)
	turtle.forward(3)
	turtle.right(135)
	turtle.forward(3)
	turtle.end_fill()

#	Define a function to draw a rectangle (room, window, door, chimney)

def draw_rectangle(x, y, color, width, hight):
	turtle.penup()
	turtle.setposition(x,y)
	turtle.setheading(0)
	turtle.pendown()
	turtle.fillcolor(color)
	turtle.begin_fill()
	turtle.forward(width)
	turtle.left(90)
	turtle.forward(hight)
	turtle.left(90)
	turtle.forward(width)
	turtle.left(90)
	turtle.forward(hight)
	turtle.left(90)
	turtle.end_fill()

#	Define a function to draw a roof

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

#	Define a function to draw multiple stars

def draw_multiple_stars():
	drawStar('green', -215,215)
	drawStar('blue', -227,219)
	drawStar('red', 235,223)
	drawStar('green', 245,227)
	drawStar('black', -255,232)
	drawStar('blue', -267,236)
	drawStar('red', 275,240)
	drawStar('green', 285,244)
	drawStar('green', -115,215)
	drawStar('blue', -127,219)
	drawStar('red', 135,223)
	drawStar('green', 145,227)
	drawStar('black', -155,232)
	drawStar('blue', -167,236)
	drawStar('red', 175,240)
	drawStar('green', 185,244)

#	Define a function to draw a house

def draw_house(x, y, windowColor): 
	draw_rectangle(x,y,'black',120,70)   			#	Draw-rooM
	draw_rectangle(100+x, 50+y,'black',-10,70)		#	Draw-chimneY
	draw_rectangle(20+x, y,'white',20,40)  			#	Draw-dooR
	draw_rectangle(80+x, 30+y, windowColor,20,20)  		#	Draw-windoW
	draw_triangle(x, 70+y,'yellow')	    			#	Draw-rooF

#	Call user-defined function

draw_multiple_stars()
draw_house(0, 0, 'magenta')
draw_house(-90, -50, 'pink')
draw_house(-250, 50, 'green')
draw_house(150, -50, 'blue')

sleep(10)

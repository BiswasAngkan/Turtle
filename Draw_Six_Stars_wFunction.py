#	Angkan Biswas
#	Date-02.04.2019
#	To draw stars with a user-defined function

import turtle
from time import sleep

#	Define a function to draw a stars

def drawStar(color, x, y):
	turtle.penup()
	turtle.setposition(x, y)
	turtle.pendown()
	turtle.fillcolor(color)


	turtle.begin_fill()
	turtle.forward(20)
	turtle.right(135)
	turtle.forward(20)
	turtle.right(-45)
	turtle.forward(20)
	turtle.right(135)
	turtle.forward(20)
	turtle.left(45)
	turtle.forward(20)
	turtle.right(135)
	turtle.forward(20)
	turtle.left(45)
	turtle.forward(20)
	turtle.right(135)
	turtle.forward(20)
	turtle.end_fill()

#	Call user-defined function
drawStar('green', 0,0)
drawStar('blue', 50,50)
drawStar('red', 150,150)
drawStar('green', 200,50)
drawStar('black', -50,-50)
drawStar('blue', -150,-150)


sleep(10)

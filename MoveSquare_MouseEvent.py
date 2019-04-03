#	Angkan Biswas
#	03.04.2019
#	To move a square by handiling a mouse event


import turtle

def mouse_handelar(x,y):
	turtle.shape('square')
	turtle.color('#7FFFD4')
	turtle.penup()
	turtle.setposition(x,y)
	turtle.pendown()

turtle.onscreenclick(mouse_handelar)
turtle.mainloop()

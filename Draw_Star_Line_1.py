#	Angkan Biswas
#	02.04.2019
#	To handle mouse event.

import turtle

def draw_line(x, y):
	turtle.shape('circle')
	turtle.color('red')
	turtle.penup()
	turtle.setposition(x, y)
	turtle.pendown()

turtle.onscreenclick(draw_line)
turtle.mainloop()




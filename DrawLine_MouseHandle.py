#	Angkan Biswas
#	02.04.2019
#	To handle mouse event.

import turtle

def draw_line(x, y):
	turtle.shape('turtle')
	turtle.color('#008000')
	turtle.setposition(x, y)

turtle.onscreenclick(draw_line)
turtle.mainloop()




#	Angkan Biswas
#	04.04.2019
#	To draw 10 circles at mouse click position



import turtle

#	A user defined function to draw a circle

def draw_circle(r,c):
	turtle.color(c)
	turtle.begin_fill()
	turtle.circle(r)
	turtle.end_fill()

#	A user defind  function to handle a mouse click.

def mouse_handle(x,y):
	turtle.penup()
	turtle.setposition(x,y)
	turtle.pendown()
	draw_circle(90,'black')
	draw_circle(80,'white')
	draw_circle(70,'#CD950C')
	draw_circle(60,'yellow')
	draw_circle(50,'#BF3EFF')
	draw_circle(40,'green')
	draw_circle(30,'black')
	draw_circle(20,'#FF7D40')
	draw_circle(10,'black')
	draw_circle(5,'green')

#	Handle mouse click
turtle.onscreenclick(mouse_handle)
turtle.mainloop()

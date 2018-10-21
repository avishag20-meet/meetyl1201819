#import turtle
#for coolness in range (5):
#	turtle.pendown()
#	turtle.forward(100)
#	turtle.right(144)
#turtle.mainloop()

#import turtle
#turtle.begin_fill()
#turtle.forward(30)
#turtle.right(90)
#turtle.forward(20)
#turtle.right(45)
#turtle.forward(25)
#turtle.right(100)
#turtle.forward(25)
#turtle.right(35)
#turtle.forward(20)
#turtle.end_fill()
#turtle.mainloop()

import turtle 
turtle.speed(0)
for i in range (400000):
	turtle.pendown()
	turtle.right(i)
	turtle.forward(200)
	turtle.right(45+i)
	turtle.forward(100)
	turtle.right(90+i)
	turtle.forward(50)
	turtle.penup()
	turtle.home()
turtle.mainloop()		

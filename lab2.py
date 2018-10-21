list1 = [134,5]
list2 = [134,6]
list3 = [] 
def ooo ():
	for i in list1:
		for ll in list2:
			if i == ll:
				list3.append(i) 
	print(list3)	
ooo()				

import turtle
turtle.penup()
turtle.goto(-110,0)
turtle.pendown()
turtle.color("blue")
turtle.circle(50)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.color("black")
turtle.circle(50)
turtle.penup()
turtle.goto(110,0)
turtle.pendown()
turtle.color("red")
turtle.circle(50)
turtle.penup()
turtle.goto(55,-50)
turtle.pendown()
turtle.color("green")
turtle.circle(50)
turtle.penup()
turtle.goto(-55,-50)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)
turtle.hideturtle()
turtle.mainloop()
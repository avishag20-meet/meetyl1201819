from turtle import Turtle 
import turtle

class Ball (Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.penup()
		self.goto(x, y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shape("circle")	
		self.shapesize(r/10)
		self.fillcolor(color)

	def move(self, screen_width, screen_heigh):
		current_x = self.xcor()
		current_y = self.ycor()
		newx = current_x + self.dx
		newy = current_y + self.dy
		right_side.ball = newx + self.r
		left_side.ball = newx + self.r
		up_side.ball = newy + self.r
		down_side.ball = newy + self.r
		self.goto(newx, newy)

		if right_side.ball > screen_width:
			self.dx = -self.dx 
		if left_side.ball > screen_width:
			self.dx = -self.dx
		if up_side.ball > screen_hight:
			self.dy = -self.dy
		if down_side.ball > screen_hight:
			self.dy = -self.dy

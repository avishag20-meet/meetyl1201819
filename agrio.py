import turtle
import math
import time
import random
import ball
from ball import Ball

turtle.tracer(1)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = [] 
MY_BALL = Ball(0, 0, 2, 2, 50, "red")

for m in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)	
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	new_ball = Ball(x, y, dx, dy, radius, color)
	BALLS.append(new_ball)

for ball in BALLS:
	ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball1, ball2):
	if ball1 == ball2:
		return False
	x1 = ball1.xcor()
	x2 = ball2.xcor()
	y1 = ball1.ycor()
	y2 = ball2.ycor()
	d = ((x1-x2)**2+(y1-y2)**2)**0.5

	if d+10 <= ball1.r+ball2.r:
	 	return True
	else: 
	 	return False	

def check_all_balls_collision():
	for ball1 in BALLS:
		for ball2 in BALLS:
			if collide(ball1, ball2):
				rad1 = ball1.r
				rad2 = ball2.r
				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)	
				dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				color = (random.random(), random.random(), random.random())					

				if ball1.r > ball2.r:
					ball2.goto(x, y)
					ball2.dx = dx
					ball2.dy = dy
					ball2.r = r
					ball2.shape("circle")	
					ball2.shapesize(r/10)
					ball2.fillcolor(color)
					ball1.r += 1
					ball1.shapesize(ball1.r/10)
turtle.mainloop()


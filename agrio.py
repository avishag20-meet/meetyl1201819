import turtle
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
MY_BALL = Ball(0, 0, 2, 2, 15, "red")

for m in range(NUMBER_OF_BALLS):
	x = random.randirt(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randirt(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)	
	dx = random.randirt(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randirt(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.rendirt(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = random.rendirt(random.random(), random.random(), random.random())
turtle.mainloop()


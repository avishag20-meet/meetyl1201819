import turtle
import math
import time
import random
import ball
from ball import Ball

turtle.bgcolor("black")

turtle.tracer(00)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

#determines balls defenitions 
NUMBER_OF_BALLS = 7
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 73
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = [] 
MY_BALL = Ball(0, 0, 2, 2, 60, "green")

for m in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)	
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	new_ball = Ball(x, y, dx, dy, radius, color)
	BALLS.append(new_ball)

def move_all_balls():
	for ball in BALLS:
		ball.move(SCREEN_WIDTH-20, SCREEN_HEIGHT-20)

#checks when balls collides
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

#borders
def draw_borders(corner_x, corner_y):
	turtle.penup()
	turtle.goto(-corner_x, -corner_y)
	turtle.pendown()
	turtle.color("red")
	turtle.goto(-corner_x, corner_y)
	turtle.goto(corner_x, corner_y)
	turtle.goto(corner_x, -corner_y)
	turtle.goto(-corner_x, -corner_y)
	turtle.penup()


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
				r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
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
				else:
					ball1.goto(x, y)
					ball1.dx = dx
					ball1.dy = dy
					ball1.r = r
					ball1.shape("circle")	
					ball1.shapesize(r/10)
					ball1.fillcolor(color)
					ball2.r += 1
					ball2.shapesize(ball2.r/10)					 

#checks what touches my ball
def check_myball_collision():
	for BALL in BALLS:
		if  collide(MY_BALL, BALL):
			myballr = MY_BALL.r
			ballr = BALL.r
			if MY_BALL.r < BALL.r:
				return False
			else:
				MY_BALL.r += 1
				MY_BALL.shapesize(MY_BALL.r/10)
				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)	
				dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				color = (random.random(), random.random(), random.random())					
				BALL.goto(x,y)
				BALL.dx = dx
				BALL.dy = dy
				BALL.r = r
	return True

#moves my ball
def movearound(event):
	x = event.x - SCREEN_WIDTH
	y = SCREEN_HEIGHT - event.y
	MY_BALL.goto (x,y)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while RUNNING:
	SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2	
	move_all_balls()
	check_all_balls_collision()
	RUNNING = check_myball_collision()
	draw_borders(SCREEN_WIDTH - 20, SCREEN_HEIGHT-20)
	turtle.update()
	time.sleep(SLEEP)

#writes game over
turtle.color("red")
turtle.goto(0,0)
turtle.write("Game over", align = "center", font = ("david" ,90, "normal"))

time.sleep(3)

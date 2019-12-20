import turtle
import os

win = turtle.Screen()
win.title("Pong V1")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Score
score1 = 0
score2 = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx = .04
ball.dy = .04

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0 Player 2 : 0", align="center", font=("Courier", 24, "normal"))

#Functions
def paddleaUp():
    y = paddleA.ycor()
    y+= 20
    paddleA.sety(y)

def paddleaDown():
    y = paddleA.ycor()
    y-= 20
    paddleA.sety(y)

def paddle_b_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddle_b_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

#Keyboard binding
win.listen()
win.onkeypress(paddleaUp, "w")
win.onkeypress(paddleaDown, "s")

win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    win.update()

    #move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system(("aplay bounce.wav&"))

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system(("aplay bounce.wav&"))

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1+=1
        pen.clear()
        pen.write("Player 1: {} Player 2 : {}".format(score1,score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2 : {}".format(score1,score2), align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system(("aplay bounce.wav&"))

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system(("aplay bounce.wav&"))


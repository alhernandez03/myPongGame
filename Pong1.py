### 10/15/2020
### Author: Alejandro Hernandez
### Simple Pong Python_3.9 Portfolio Project

import turtle

wn = turtle.Screen()
wn.title("Pong by @alejandrohernandezphoto")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


#Score


# Player 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Player 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball Alpha
ball_a = turtle.Turtle()
ball_a.speed(0)
ball_a.shape("square")
ball_a.color("white")
ball_a.shapesize(stretch_wid=1, stretch_len=1)
ball_a.penup()
ball_a.goto(0, 0)
ball_a.dx = 0.7
ball_a.dy = 0.7


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard Binding
wn.listen()

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main Game Loop
while True:
    wn.update()

    # Move the Ball
    ball_a.setx(ball_a.xcor() + ball_a.dx)
    ball_a.sety(ball_a.ycor() + ball_a.dy)

    # Border Checking
    if ball_a.ycor() > 290:
        ball_a.sety(290)
        ball_a.dy *= -1

    if ball_a.ycor() < -290:
        ball_a.sety(-290)
        ball_a.dy *= -1

    if ball_a.xcor() > 390:
        ball_a.goto(0, 0)
        ball_a.dx *= -1

    if ball_a.xcor() < -390:
        ball_a.goto(0, 0)
        ball_a.dx *= -1
        
    # Paddle and Ball Collision
    if (ball_a.xcor() > 340 and ball_a.xcor() < 350) and (ball_a.ycor() < paddle_b.ycor() + 40 and ball_a.ycor() > paddle_b.ycor() -40):
        ball_a.setx (340)
        ball_a.dx *= -1

    if (ball_a.xcor() < -340 and ball_a.xcor() > -350) and (ball_a.ycor() < paddle_a.ycor() + 40 and ball_a.ycor() > paddle_a.ycor() -40):
        ball_a.setx (-340)
        ball_a.dx *= -1




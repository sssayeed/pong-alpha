# This is a remake of the classic game Pong, I wanna start by making
# the classic game and add more features in the future.
# By SK Sadman Sayeed

# using turtle for the GUI for now, will change to a more complex one later

import turtle
from Paddle import Paddle
from Ball import Ball

# Game Window
window = turtle.Screen()
window.title("Pong Alpha")
window.bgcolor("black")     # will add feature to customize colors later
window.setup(width=800, height=600)  # 600p
window.tracer(0)    # manual updating

border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-390, 250)
border.pendown()
border.goto(390, 250)
border.goto(390, -250)
border.goto(-390, -250)
border.goto(-390, 250)
border.penup()
border.hideturtle()

# Paddles
paddle1 = Paddle(-350, 0)
paddle2 = Paddle(350, 0)

# Ball
ball = Ball()

# Scoring
score1 = 0
score2 = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 | Player 2: 0", align="center", font=("Courier", 20, "normal"))

# Movement
window.listen()
window.onkeypress(paddle1.paddle_up, "w")
window.onkeypress(paddle1.paddle_down, "s")

# Game Loop
while True:
    window.update()

    # move ball
    ball.ball.setx(ball.ball.xcor() + ball.dx)
    ball.ball.sety(ball.ball.ycor() + ball.dy)

    # bounce back form borders
    if ball.ball.ycor() > 250:
        ball.ball.sety(250)
        ball.dy *= -1
    if ball.ball.ycor() < -250:
        ball.ball.sety(-250)
        ball.dy *= -1

    # return to the centre if missed
    if ball.ball.xcor() > 390:
        ball.ball.goto(0, 0)
        score1 += 1
        ball.dx *= -1
        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(score1, score2), align="center", font=("Courier", 20, "normal"))
    if ball.ball.xcor() < -390:
        ball.ball.goto(0, 0)
        score2 += 1
        ball.dx *= -1
        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(score1, score2), align="center", font=("Courier", 20, "normal"))

    # collisions
    if (ball.ball.xcor() > 340 and ball.ball.xcor() < 350) and (ball.ball.ycor() < paddle2.paddle.ycor() + 40 and ball.ball.ycor() > paddle2.paddle.ycor() - 40):
        ball.ball.setx(340)
        ball.dx *= -1

    if (ball.ball.xcor() < -340 and ball.ball.xcor() > -350) and (ball.ball.ycor() < paddle1.paddle.ycor() + 40 and ball.ball.ycor() > paddle1.paddle.ycor() - 40):
        ball.ball.setx(-340)
        ball.dx *= -1

    # move AI paddle
    if ball.ball.ycor() > paddle2.paddle.ycor() + 4:
        paddle2.paddle_up()
    elif ball.ball.ycor() < paddle2.paddle.ycor() - 4:
        paddle2.paddle_down()

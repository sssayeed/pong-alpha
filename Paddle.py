import turtle


class Paddle:

    def __init__(self, coordx, coordy):
        self.paddle = turtle.Turtle()
        self.x = coordx
        self.y = coordy
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(coordx, coordy)

    def paddle_up(self):
        if self.paddle.ycor() >= 200:
            return
        curr_y = self.paddle.ycor()
        curr_y += 10
        self.paddle.sety(curr_y)

    def paddle_down(self):
        if self.paddle.ycor() <= -200:
            return
        curr_y = self.paddle.ycor()
        curr_y -= 10
        self.paddle.sety(curr_y)

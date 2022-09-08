from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, screen_width, screen_height, position) -> None:
        super().__init__()
        self.shape("square")
        self.speed('fastest')
        self.hideturtle()
        self.resizemode('user')
        self.penup()
        if position == "left":
            self.goto(- (screen_width/2 -20), 0)
        else:
            self.goto(screen_width/2 -20, 0)
        self.showturtle()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.screen_height = screen_height

    def move_up(self):
        if not self.ycor() >= self.screen_height/2 - 50:
            self.goto(self.xcor(), self.ycor() + 10)

    def move_down(self):
        if not self.ycor() <= - self.screen_height/2 + 50:
            self.goto(self.xcor(), self.ycor() - 10)
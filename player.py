from turtle import Turtle
FINISH_LINE_Y=280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)
        self.left(90)
    def go_to_start(self):
        self.goto(0,-280)
    def t_forward(self):
        self.forward(10)

    def t_backward(self):
        self.backward(10)

    def is_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False



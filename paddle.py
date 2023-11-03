from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        for i in range(2):
            self.shape("square")
            self.turtlesize(stretch_wid=5, stretch_len=1)
            self.color("white")
            self.penup()
            self.goto(position)


    def go_up(self):
        new_y_pos = self.ycor() + 20
        self.goto(self.xcor(), new_y_pos)

    def go_down(self):
        new_pos = self.ycor() - 20
        self.goto(self.xcor(), new_pos)


    # def up_for_left(self):
    #     new_y_pos = self.ycor() + 20
    #     self.goto(self.xcor(), new_y_pos)
    #
    # def down_for_left(self):
    #     new_pos = self.ycor() - 20
    #     self.goto(self.xcor(), new_pos)
    #
    # def up_for_right(self):
    #     new_y_pos = self.ycor() + 20
    #     self.goto(self.xcor(), new_y_pos)
    #
    # def down_for_right(self):
    #     new_pos = self.ycor() - 20
    #     self.goto(self.xcor(), new_pos)

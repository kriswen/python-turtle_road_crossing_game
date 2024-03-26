from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-230, 270)
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-230, 270)
        self.write(arg=f"Level: {self.level}", move=False, align="Center", font=FONT)
        self.display_crossing_line()

    def level_up(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="Center", font=FONT)

    def display_crossing_line(self):
        for x_axis in range(300, -300, -20):
            self.goto(x_axis, 270)
            self.write(arg="_", move=False, align="Center", font=FONT)
        for x_axis in range(300, -300, -20):
            self.goto(x_axis, -250)
            self.write(arg="_", move=False, align="Center", font=FONT)
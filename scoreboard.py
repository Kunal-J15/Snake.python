from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.score = -1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-300, 300)
        self.update()

    def update(self):
        self.clear()
        self.goto(-300, 300)
        self.score += 1
        self.write(f"Score {self.score}", True, align="center",font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", True, align="center", font=('Arial', 15, 'normal'))

    def reset(self):
        self.clear()
        self.__init__()
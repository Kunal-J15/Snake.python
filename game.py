from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Snake Game")
        self.screen.listen()
        self.screen.screensize(500, 500)
        self.screen.bgcolor("black")

    def play(self):
        self.screen.tracer(0)
        a = Snake()
        b = Food()
        c = ScoreBoard()
        self.screen.update()
        self.screen.onkey(a.turn_left, "a")
        self.screen.onkey(a.turn_right, "d")
        self.screen.onkey(a.turn_up, "w")
        self.screen.onkey(a.turn_down, "s")
        game_is_on = True
        while game_is_on:
            self.screen.tracer(0)
            a.move()
            time.sleep(0.1)
            self.screen.update()
            if a.head.xcor() > 360 or a.head.xcor() < -360 or a.head.ycor() > 310 or a.head.ycor() < -310:
                game_is_on = False
                c.game_over()
            if a.head.distance(b.position()) < 20:
                a.add_part()
                b.rand_loc()
                c.update()
            for _ in range(3, len(a.body) - 1):
                if a.head.distance(a.body[_].position()) < 15:
                    game_is_on = False
                    c.game_over()


d = Game()
d.play()


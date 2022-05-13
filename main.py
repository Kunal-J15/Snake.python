from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def reset():
    a.reset()
    b.reset()
    c.reset()
    play()


def play():
    cheat = True
    screen.onkey(a.turn_right, "d")
    screen.onkey(a.turn_left, "a")
    screen.onkey(a.turn_up, "w")
    screen.onkey(a.turn_down, "s")
    screen.onkey(a.pause, "p")
    game_is_on = True
    while game_is_on:
        screen.tracer(0)
        a.move()
        time.sleep(0.1)
        screen.update()
        if (a.head.xcor() > 360 or a.head.xcor() < -360 or a.head.ycor() > 310 or a.head.ycor() < -310) and cheat:
            game_is_on = False
            c.game_over()
        if a.head.distance(b.position()) < 20:
            a.add_part()
            b.rand_loc()
            c.update()
        for _ in range(3, len(a.body)-1):
            if a.head.distance(a.body[_].position()) < 15 and cheat:
                game_is_on = False
                c.game_over()


screen = Screen()
screen.tracer(0)
a = Snake()
b = Food()
c = ScoreBoard()
screen.update()
screen.title("Snake Game")
screen.listen()
screen.screensize(500,500)
screen.bgcolor("black")
screen.onkey(reset, "r")
play()
screen.exitonclick()


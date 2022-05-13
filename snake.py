from turtle import Turtle


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.head.color("grey")
        self.pauser = False

    def add_part(self):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        x_pos = self.body[len(self.body)-1].xcor()
        y_pos = self.body[len(self.body)-1].ycor()
        new_part.goto(x_pos, y_pos)
        self.body.append(new_part)

    def create_snake(self):
        for _ in range(0, 3):
            new_part = Turtle("square")
            new_part.color("white")
            new_part.penup()
            new_part.backward(20 * _)
            self.body.append(new_part)

    def move(self):
        if not self.pauser:
            for part in range(len(self.body)-1, 0, -1):
                new_x = self.body[part-1].xcor()
                new_y = self.body[part-1].ycor()
                self.body[part].goto((new_x, new_y))
            self.body[0].forward(20)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def reset(self):
        for _ in self.body:
            _.reset()
            del _
        self.__init__()

    def pause(self):
        self.pauser = not self.pauser






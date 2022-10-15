import turtle
import random

s = turtle.Screen()
s.screensize(400, 400)
s.setup(420, 420)
w, h = s.screensize()
s.bgpic("images/bg.gif")
s.tracer(0)


class Display:
    def __init__(self):
        self.type = turtle.Turtle()
        self.lives = 3
        self.level = 1

    def end(self):
        s.bgpic("images/end.gif")
        self.type.goto(0, 148)
        # noinspection PyTypeChecker
        self.type.write(f"LOSSINGS HOGAYA  \n", align='center',
                        font=("Times New Roman", "20", "normal"))
        self.type.goto((0,145))
        self.type.write(f"HIGH SCORE:{self.level} ", align='center',
                        font=("Times New Roman", "20", "normal"))

    def update(self):
        self.type.clear()
        self.type.penup()
        self.type.hideturtle()
        self.type.goto(0, 160)
        # noinspection PyTypeChecker
        self.type.write(f'Lives:{self.lives} Level: {self.level} ', align='center',
                        font=("Times New Roman", "18", "italic"))


class Character:
    def __init__(self, start_position, position, position_change, radius, shape):
        s.addshape(shape)
        self.type = turtle.Turtle()
        self.type.shape(shape)
        self.type.penup()
        self.start_position = start_position
        self.position = position
        self.position_change = position_change
        self.radius = radius

    def update(self):
        self.position[0] += self.position_change[0]
        self.position[1] += self.position_change[1]
        if self.position[1] < -(h / 2):
            self.position[1] = h / 2
        elif self.position[1] > (h / 2):
            self.position[1] = -h / 2
        elif self.position[0] > (w / 2):
            self.position[0] = -w / 2
        elif self.position[0] < -(w / 2):
            self.position[0] = w / 2
        self.type.goto(self.position[0], self.position[1])

    def reset(self):
        self.position[0] = self.start_position[0]
        self.position[1] = self.start_position[1]
        if self == door:
            self.position[1] = random.randint(-180, 180)

    def in_collision(self, obj):
        x1 = self.position[0]
        x2 = obj.position[0]
        y1 = self.position[1]
        y2 = obj.position[1]

        radius1 = self.radius
        radius2 = obj.radius
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # distance formula

        if distance < radius1 + radius2:
            return True
        else:
            return False


display = Display()
player = Character([-175, 0], [-175, 0], [0, 0], 15, "images/kanye.gif")
harm1 = Character([-125, 0], [-125, 0], [0, -.2], 25, "images/pete.gif")
harm2 = Character([-75, 0], [-75, 0], [0, .15], 25, "images/pete.gif")
harm3 = Character([-25, 0], [-25, 0], [0, .2], 25, "images/pete.gif")
harm4 = Character([25, 0], [25, 0], [0, .075], 25, "images/pete.gif")
harm5 = Character([75, 0], [75, 0], [0, -.13], 25, "images/pete.gif")
harm6 = Character([125, 0], [125, 0], [0, .1], 25, "images/pete.gif")
door = Character([175, 100], [175, 100], [0, 0], 25, "images/kim.gif")


def up():
    player.position[1] += 25


def down():
    player.position[1] -= 25


def right():
    player.position[0] += 25


def left():
    player.position[0] -= 25


harm = [harm1, harm2, harm3, harm4, harm5, harm6]


def animation():
    while display.lives > 0:
        display.update()
        player.update()
        door.update()
        for obj in harm:
            if player.in_collision(obj):
                display.lives -= 1
                player.reset()
                obj.reset()
            obj.update()

        if player.position[0]<-175:
            player.reset()

        if player.in_collision(door):
            display.level += 1
            for obj in harm:
                obj.reset()
                obj.position_change[1] *= 1.3
            player.reset()
            door.reset()


        s.listen()
        s.onkeypress(up, "Up")
        s.onkeypress(left, "Left")
        s.onkeypress(down, "Down")
        s.onkeypress(right, "Right")
        s.update()

    s.clear()
    display.end()
    s.mainloop()
    s.update()


animation()

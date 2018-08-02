import turtle
import random

class Snake(turtle.Turtle):
    number = 0
    bodyPos = []
    torwarding = 0
    over = False

    def __init__(self, color):
        turtle.Turtle.__init__(self)
        self.ht()
        self.length = 3
        self.color(color)
        self.speed(10)

    def draw(self):
        self.up()
        self.shape("circle")
        self.shapesize(0.2)
        self.keyListening()
        self.move()

    def keyListening(self):
        turtle.onkeypress(self.u, "Up")
        turtle.onkeypress(self.l, "Left")
        turtle.onkeypress(self.r, "Right")
        turtle.onkeypress(self.d, "Down")
        turtle.listen()

    def u(self):
        if self.torwarding == 270:
            pass
        else:
            self.torwarding = 90

    def d(self):
        if self.torwarding == 90:
            pass
        else:
            self.torwarding = 270

    def l(self):
        if self.torwarding == 0:
            pass
        else:
            self.torwarding = 180

    def r(self):
        if self.torwarding == 180:
            pass
        else:
            self.torwarding = 0

    def isOver(self):
        x = self.xcor()
        y = self.ycor()
        if(x < -220 or x > 220 or
           y > 220 or y < -220):
            self.overScene()

    def overScene(self):
        self.over = True
        turtle.clear()
        self.clear()
        self.setposition(0, 0)
        turtle.setposition(0, 0)
        turtle.write("Game over", align="center",
                     font=("Arial", 20, "bold"))

    def move(self):

        self.up()
        self.setheading(self.torwarding)
        self.stamp()
        self.fd(10)
        x = round(self.xcor())
        y = round(self.ycor())
        if self.number > self.length:
            self.clearstamps(1)
            self.bodyPos.append([x, y])
            self.bodyPos.pop(-1)
        else:
            self.bodyPos.append([x, y])
            self.number += 1
        self.isOver()
        turtle.ontimer(self.move, 80)


class bonus(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        x = random.randrange(-10, 10, 1)
        y = random.randrange(-10, 10, 1)
        self.hideturtle()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("red")
        self.penup()
        self.goto(x*20, y*20)
        self.stamp()


class border:
    def draw(self):
        turtle.ht()
        turtle.clear()
        turtle.pu()
        turtle.speed(0)
        turtle.pensize(20)
        turtle.color("grey")
        turtle.goto(-230, 230)
        turtle.pd()
        turtle.goto(230, 230)
        turtle.goto(230, -230)
        turtle.goto(-230, -230)
        turtle.goto(-230, 230)
        turtle.pu()
        turtle.goto(0, 0)


class game:
    state = 'null'

    def welcome(self):
        self.state = "welcome"
        turtle.clear()
        turtle.hideturtle()
        turtle.up()
        turtle.pensize(2)
        colors = ["red", "yellow", "purple", "blue"]
        turtle.setposition(-150, 20)
        turtle.tracer(False)
        turtle.pd()
        for x in range(40):
            turtle.forward(2*x)
            turtle.color(colors[x % 4])
            turtle.left(91)
        turtle.setposition(75, 0)
        turtle.write("Welcome to Snake Game", align="center",
                     font=("Arial", 20, "bold"))
        turtle.setposition(15, -35)
        turtle.write("Press G to begin", align="center",
                     font=("Arial", 20, "normal"))
        self.keyListening()

    def start(self):
        turtle.onkey(None, key="g")
        self.state = "stated"
        try:
            self.snake.clear()
            turtle.clear()
            self.border = border()
            self.snake = Snake('blue')
            self.border.draw()
            self.snake.draw()
            self.bonus = bonus()

            self.genBonus()
            self.eating()

        except:
            self.border = border()
            self.snake = Snake('blue')
            self.border.draw()
            self.snake.draw()
            self.bonus = bonus()

            self.genBonus()
            self.eating()

    def eating(self):
        if (self.bonus != None and self.snake.xcor() < self.bonus.xcor()+0.5 and self.snake.xcor() > self.bonus.xcor()-0.5 and self.snake.ycor() < self.bonus.ycor() + 0.5 and self.snake.ycor() > self.bonus.ycor() - 0.5):
            self.snake.length += 1
            self.bonus.clear()
            self.bonus = None
        turtle.ontimer(self.eating, 20)

    def genBonus(self):
        if self.bonus == None and self.snake.over==False:
            print("1")
            self.bonus = bonus()
        turtle.ontimer(self.genBonus, 2000)

    def keyListening(self):
        if(self.state == 'welcome'):
            turtle.onkey(self.start, "g")
            turtle.listen()
        else:
            turtle.onkey(None, key="g")


if __name__ == "__main__":
    game = game()
    game.welcome()
    turtle.done()

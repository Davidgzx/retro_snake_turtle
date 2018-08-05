import turtle
import random


class Snake(turtle.Turtle):
    number = 0
    bodyPos = []
    torwarding = 0

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
        turtle.onkeypress(self.turnUp, "Up")
        turtle.onkeypress(self.turnLeft, "Left")
        turtle.onkeypress(self.turnRight, "Right")
        turtle.onkeypress(self.turnDown, "Down")
        turtle.listen()

    def turnUp(self):
        if self.torwarding == 270:
            pass
        else:
            self.torwarding = 90

    def turnDown(self):
        if self.torwarding == 90:
            pass
        else:
            self.torwarding = 270

    def turnLeft(self):
        if self.torwarding == 0:
            pass
        else:
            self.torwarding = 180

    def turnRight(self):
        if self.torwarding == 180:
            pass
        else:
            self.torwarding = 0

    def move(self):
        self.up()
        self.color = 'red'
        self.setheading(self.torwarding)
        self.fd(10)
        self.stamp()
        x = round(self.xcor())
        y = round(self.ycor())
        if self.number > self.length:
            self.clearstamps(1)
            self.bodyPos.append([x, y])
            self.bodyPos.pop(0)
        else:
            self.bodyPos.append([x, y])
            self.number += 1
        turtle.ontimer(self.move, 80)


class bonus(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("red")
        self.penup()

    def gen(self):
        x = random.randrange(-200, 200, 10)
        y = random.randrange(-200, 200, 10)
        self.goto(x, y)
        return [self.stamp(), x, y]


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
    bonusList = []

    def welcome(self):
        self.state = "welcome"
        turtle.clear()
        turtle.hideturtle()
        turtle.up()
        turtle.pensize(1)
        colors = ["#FFAA00", "#BF8F30", "#A66F00", "#FFBF40", "#FFD073", "#3914AF",
                  "#3914AF", "#412C84", "#200772", "#6A48D7", "#876ED7", "#009999",
                  "#1D7373", "#412C84", "#006363", "#5CCCCC", "#33CCCC"]
        turtle.setposition(-150, 20)
        turtle.tracer(False)
        turtle.pd()
        for x in range(60):
            turtle.fd(x/4)
            turtle.dot(15)

            turtle.color(colors[random.randrange(0, 15, 1)])
            turtle.left(15)

        turtle.setposition(75, -30)
        turtle.write("Welcome to Snake Game\n\nPress G to begin", align="center",
                     font=("Arial", 20, "bold"))
        self.keyListening()

    def start(self):
        turtle.onkey(None, key="g")
        self.state = "started"
        turtle.clear()
        self.border = border()
        self.bonus = bonus()
        self.snake = Snake('blue')
        self.border.draw()
        self.snake.draw()
        self.isOver()
        self.genBonus()
        self.eatBonus()

    def overScene(self):
        self.state = 'over'
        turtle.clear()
        self.snake.clear()
        self.bonus.clear()
        self.bonusList.clear()
        turtle.setposition(0, 0)
        turtle.write("Game over\nPress G to restart", align="center",
                     font=("Arial", 20, "bold"))
        self.keyListening()

    def isOver(self):
        x = self.snake.xcor()
        y = self.snake.ycor()
        if(x < -220 or x > 220 or
           y > 220 or y < -220):
            self.overScene()
        for i in self.snake.bodyPos:
            if self.snake.bodyPos.count(i) > 1:
                self.overScene()
        if self.state == 'started':
            turtle.ontimer(self.isOver, 20)

    def eatBonus(self):
        # print(self.bonusList[0])
        # print([self.snake.xcor(),self.snake.ycor()])
        if (len(self.bonusList) > 0 and self.snake.xcor() < self.bonusList[0][1]+1 and self.snake.xcor() > self.bonusList[0][1] - 1 and self.snake.ycor() < self.bonusList[0][2] + 1 and self.snake.ycor() > self.bonusList[0][2] - 1):
            self.snake.length += 1
            id = self.bonusList.pop()[0]
            self.bonus.clearstamp(id)

        turtle.ontimer(self.eatBonus, 20)

    def genBonus(self):
        if len(self.bonusList) == 0 and self.state == "started":
            self.bonusList.append(self.bonus.gen())
        if self.state == 'started':
            turtle.ontimer(self.genBonus, 20)

    def keyListening(self):
        if(self.state == 'welcome' or self.state == 'over'):
            turtle.onkey(self.start, "g")
            turtle.listen()
        else:
            turtle.onkey(None, key="g")


if __name__ == "__main__":
    game = game()
    game.welcome()
    turtle.done()

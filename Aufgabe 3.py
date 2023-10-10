from turtle import *
i = 1
geti = Turtle()


geti.penup()
geti.goto(-200, -200)
geti.pendown()

geti.color("yellow")

geti.begin_fill()

for i in range(4):
    geti.forward(400)
    geti.left(90)
geti.end_fill()

geti.penup()
geti.goto(50, 0)
geti.pendown()

geti.color("blue")

geti.begin_fill()

for i in range(4):
    geti.forward(100)
    geti.left(90)
geti.end_fill()

geti.penup()
geti.goto(-150, -195)
geti.pendown()

geti.color("grey")

geti.begin_fill()

for i in range(2):
  geti.forward(150)
  geti.left(90)
  geti.forward(300)
  geti.left(90)
geti.end_fill()

geti.penup()
geti.goto(-200, 200)
geti.pendown()

geti.color("red")
geti.begin_fill()

geti.left(30)
geti.forward(230.94)
geti.goto(200, 200)
geti.end_fill()

geti.penup()
geti.goto(0, 0)
geti.pendown()



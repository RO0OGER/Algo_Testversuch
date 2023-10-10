from turtle import *

violett = Turtle()
blau = Turtle()
gruen = Turtle()
gelb = Turtle()
orange = Turtle()
rot = Turtle()
i = 1

violett.color("violet")
blau.color("blue")
gruen.color("green")
gelb.color("yellow")
orange.color("orange")
rot.color("red")

violett.lt(90)
blau.lt(90)
gruen.lt(90)
gelb.lt(90)
orange.lt(90)
rot.lt(90)

violett.penup()
violett.goto(150, 0)
violett.pendown()

blau.penup()
blau.goto(150, 0)
blau.pendown()

gruen.penup()
gruen.goto(150, 0)
gruen.pendown()

gelb.penup()
gelb.goto(150, 0)
gelb.pendown()

orange.penup()
orange.goto(150, 0)
orange.pendown()

rot.penup()
rot.goto(150, 0)
rot.pendown()

violett.begin_fill()
violett.circle(150,180)
violett.lt(90)
violett.forward(40)
violett.lt(90)
violett.circle(-110,180)
violett.lt(90)
violett.forward(40)


blau.goto(190, 0)
blau.circle(190, 180)
blau.lt(90)
blau.forward(40)

gruen.goto(230, 0)
gruen.circle(230, 180)
gruen.lt(90)
gruen.forward(40)

gelb.goto(270, 0)
gelb.circle(270, 180)
gelb.lt(90)
gelb.forward(40)

orange.goto(310, 0)
orange.circle(310, 180)
orange.lt(90)
orange.forward(40)

rot.goto(350, 0)
rot.circle(350, 180)
rot.lt(90)
rot.forward(40)


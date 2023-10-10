import random
from turtle import*

farben = ("blue", "yellow","red", "green")
winkel = 0
speed(20)
fillcolor("white")
while winkel != 72:
    pencolor(random.choice(farben))
    winkel+= 1
    forward(100)
    lt(5)
    penup()
    goto(0 ,0)
    pendown()
goto(0, -20)
pencolor("white")
begin_fill()
circle(20)
pencolor("white")
end_fill()
pencolor("green")
goto(0, -100)
circle(100)


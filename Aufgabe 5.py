from turtle import *
winkel = 90
i=0
o = 200


penup()
goto(-200, -200)
pendown()

 
while o > -200:
    o = o -40
    goto(200, o)
    goto(-200, -200)


while o <= 200:
    goto(o, 200)
    o = o +40
    goto(-200, -200)

penup()
goto(200, -200)
pendown()

 
while o > -200:
    o = o -40
    goto(o , 200)
    goto(200, -200)


while o <= 200:
    goto(-200, o)
    o = o +40
    goto(200, -200)

penup()
goto(-200, 200)
pendown()

forward(400)
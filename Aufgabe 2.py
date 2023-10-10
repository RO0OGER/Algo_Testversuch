import random
from turtle import *


geti = Turtle()
input_user = int(input("Bitte Zahl eingeben: "))
x = random.randint(-500, 500)
y = random.randint(-500, 500)


for x in range(input_user):
   x = random.randint(-500, 500)
   y = random.randint(-500, 500)
   geti.circle(random.randint(5, 100), 360)
   geti.penup()
   geti.goto(y, x)
   geti.pendown()


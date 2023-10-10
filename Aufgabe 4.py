from turtle import *

ecken = int(input("Sag Ecke Bruder: "))
winkel = 0
i = ecken

winkel = 360/ecken

while i > 0:
    forward(100)
    left(winkel)
    i-=1






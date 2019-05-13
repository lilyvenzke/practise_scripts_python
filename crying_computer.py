#I just wanted to make my computer cry/show emotion
import turtle

window = turtle.Screen()
eyes = turtle.Turtle()   
eyes.pensize(8)
eyes.penup()
eyes.setposition(-150,100)
eyes.pendown()
eyes.circle(20)

eyes.penup()
eyes.setposition(150,100)
eyes.pendown()
eyes.circle(20)
while True:
    cryingL = turtle.Turtle()
    cryingR = turtle.Turtle()
    L = 10
    R = 10
    cryingL.pensize(4)
    cryingR.pensize(4)
    leftpos = -20
    rightpos = -20
    cryingL.right(90)
    cryingR.right(90)
    for i in range(1, 10):
       cryingL.penup()
       cryingR.penup()
       cryingL.setposition(-140, leftpos * i)
       cryingR.setposition(140, rightpos * i)
       cryingL.pendown()
       cryingR.pendown()
       cryingL.forward(L)
       cryingR.forward(R)
    cryingL.clear()
    cryingR.clear()
   
    
#crying()

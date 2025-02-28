import turtle as t
import time
from random import randint

delay=0.1
bodyParts = []

#make the screen
wn = t.Screen()
wn.bgcolor("ivory4")
wn.setup(width=600,height=600)

#Make the head of the snake
head = t.Turtle(shape="square")
head.speed(0)
head.penup()
head.direction="stop"

# Make the food
food = t.Turtle(shape="turtle")
food.speed(0)
food.penup()
food.teleport(100,100)
food.color("red")

#GameOver
def hideTheBody():
        global bodyParts
        head.teleport(0,0)
        head.direction="stop"
        for eachPart in bodyParts:
            eachPart.hideturtle()
        bodyParts = []

def addPart():
    bodyPart= t.Turtle(shape="circle")
    bodyPart.speed(0)
    bodyPart.penup()
    bodyParts.append(bodyPart)

def move():
    if head.direction == "up":
        head.sety(head.ycor()+20)
    elif head.direction == "down":
        head.sety(head.ycor()-20)
    elif head.direction == "left":
        head.setx(head.xcor()-20)
    elif head.direction == "right":
        head.setx(head.xcor()+20)

#Set Direction

def up():
    if head.direction != "down":
        head.direction="up"
def down():
    if head.direction != "up":
        head.direction="down"
def right():
    if head.direction != "left":
        head.direction="right"
def left():
    if head.direction != "right":
        head.direction="left"

#Check for inputs
wn.onkeypress(up,"w")
wn.onkeypress(down,"s")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
#Game Loop
wn.listen()
while True:
    wn.update()
    # Check for edge collisions
    if head.ycor()>290 or head.ycor()<-290 or head.xcor()>290 or head.xcor()<-290:
        hideTheBody()
    #Check for food collisions
    if (abs(head.xcor()-food.xcor()) <=19) and (abs(head.ycor()-food.ycor()) <=19):
        food.teleport(randint(-290,290),randint(-290,290))
        addPart()
    #Move body parts
    for i in range(len(bodyParts)-1,0,-1):
        newX= bodyParts[i-1].xcor()
        newY= bodyParts[i-1].ycor()
        bodyParts[i].teleport(newX,newY)
    if len(bodyParts)>0:
        newX = head.xcor()
        newY = head.ycor()
        neck = bodyParts[0]
        neck.teleport(newX,newY)
    move()
    #Check for body collisons
    for eachBodyPart in bodyParts:
        if head.distance(eachBodyPart)<10:
            hideTheBody()
    time.sleep(delay)
import turtle as t
import time
from random import randint

delay=0.1
bodyParts = []
snakebodyParts = []
global newX
global newY
global snewY
global snewX
#make the screen
wn = t.Screen()
wn.bgcolor("ivory4")
wn.setup(width=600,height=600)

#Make the head of the snake
head = t.Turtle(shape="square")
head.color("red")
head.speed(0)
head.penup()
head.direction="stop"
#make the head of snake player 2
#Make the head of the snake
snakeHead = t.Turtle(shape="square")
snakeHead.speed(0)
snakeHead.penup()
snakeHead.direction="stop"
# Make the food
food = t.Turtle(shape="turtle")
food.speed(0)
food.penup()
food.teleport(100,100)
food.color("red")

#GameOver
def hideTheBody(snake):
        snake.teleport(0,0)
        snake.direction="stop"
        if snake == head:
            global bodyParts
            for eachPart in bodyParts:
                eachPart.hideturtle()
            bodyParts = []
        elif snake == snakeHead:
            global snakebodyParts
            for eachPart in snakebodyParts:
                eachPart.hideturtle()
            snakebodyParts = []

def addPart(snake):
    if snake == head:
        global bodyParts
        bodyPart= t.Turtle(shape="circle")
        bodyPart.speed(0)
        bodyPart.penup()
        bodyParts.append(bodyPart)
    elif snake == snakeHead:
        global snakebodyParts
        snakebodyPart= t.Turtle(shape="circle")
        snakebodyPart.speed(0)
        snakebodyPart.penup()
        snakebodyParts.append(snakebodyPart) 

def move():
    if head.direction == "up":
        head.sety(head.ycor()+20)
    elif head.direction == "down":
        head.sety(head.ycor()-20)
    elif head.direction == "left":
        head.setx(head.xcor()-20)
    elif head.direction == "right":
        head.setx(head.xcor()+20)
    if snakeHead.direction == "up":
        snakeHead.sety(snakeHead.ycor()+20)
    elif snakeHead.direction == "down":
        snakeHead.sety(snakeHead.ycor()-20)
    elif snakeHead.direction == "left":
        snakeHead.setx(snakeHead.xcor()-20)
    elif snakeHead.direction == "right":
        snakeHead.setx(snakeHead.xcor()+20)

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

def upa():
    if snakeHead.direction != "down":
        snakeHead.direction="up"
def downa():
    if snakeHead.direction != "up":
        snakeHead.direction="down"
def righta():
    if snakeHead.direction != "left":
        snakeHead.direction="right"
def lefta():
    if snakeHead.direction != "right":
        snakeHead.direction="left"

def checkEdge(snake):
    if snake.ycor()>290 or snake.ycor()<-290 or snake.xcor()>290 or snake.xcor()<-290:
        hideTheBody(snake)

def checkFood(snake):
        if (abs(snake.xcor()-food.xcor()) <=19) and (abs(snake.ycor()-food.ycor()) <=19):
            food.teleport(randint(-290,290),randint(-290,290))
            addPart(snake)

def moveBodyPart(snake):
    if snake == head:
        for i in range(len(bodyParts)-1,0,-1):
            newX= bodyParts[i-1].xcor()
            newY= bodyParts[i-1].ycor()
            bodyParts[i].teleport(newX,newY)
            if len(bodyParts)>0:
                newX = head.xcor()
                newY = head.ycor()
                neck = bodyParts[0]
                neck.teleport(newX,newY)
    elif snake == snakeHead:
        for i in range(len(snakebodyParts)-1,0,-1):
            snewX= snakebodyParts[i-1].xcor()
            snewY= snakebodyParts[i-1].ycor()
            snakebodyParts[i].teleport(snewX,snewY)
        if len(snakebodyParts)>0:
            snewX = snakeHead.xcor()
            snewY = snakeHead.ycor()
            sneck = snakebodyParts[0]
            sneck.teleport(snewX,snewY)

#Check for inputs
wn.onkeypress(upa,"w")
wn.onkeypress(downa,"s")
wn.onkeypress(lefta,"a")
wn.onkeypress(righta,"d")
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
#Game Loop
wn.listen()
while True:
    wn.update()
    # Check for edge collisions
    checkEdge(head)
    checkEdge(snakeHead)
    #Check for food collisions
    checkFood(head)
    checkFood(snakeHead)
    #Move body parts
    moveBodyPart(head)
    moveBodyPart(snakeHead)

    move()
    #Check for body collisons
    if len(bodyParts) > 0:
        for eachBodyPart in bodyParts:
            if head.distance(eachBodyPart)<10:
                hideTheBody(head)
        for eachBodyPart in bodyParts:
            if snakeHead.distance(eachBodyPart)<10:
                hideTheBody(snakeHead)
    if len(snakebodyParts) > 0:            
        for eachBodyPart in snakebodyParts:
            if snakeHead.distance(eachBodyPart)<10:
                hideTheBody(snakeHead)
        for eachBodyPart in snakebodyParts:
            if head.distance(eachBodyPart)<10:
                hideTheBody(head)
    time.sleep(delay)
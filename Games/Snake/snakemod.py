import turtle as t
import time
import winsound
from random import randint, random


global paused
global speed
global newX
global newY
global snewY
global snewX
speed = 1
delay=0.1*speed

bodyParts = []
paused = False
snakebodyParts = []
dup = 90
ddown = -90
dleft = 180
dright = 0

#make the screen
wn = t.Screen()
#mod for 3
wn.title("Snake By Eli")
wn.bgcolor("ivory4")
wn.setup(width=600,height=600)


#Make the head of the snake
head = t.Turtle(shape="turtle")
head.color("red")
head.speed(0)
head.penup()
head.direction="stop"
#make the head of snake player 2
snakeHead = t.Turtle(shape="turtle")
snakeHead.speed(0)
snakeHead.penup()
snakeHead.direction="stop"
# Make the food
food = t.Turtle(shape="circle")
food.speed(0)
food.penup()
food.teleport(100,100)
food.color("red")

#GameOver
def hideTheBody(snake):
        #mod for 18
        winsound.PlaySound('windowserror.wav', winsound.SND_ASYNC)
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
        global tail
        bodyPart= t.Turtle(shape="circle")
        bodyPart.speed(0)
        bodyPart.penup()
        bodyParts.append(bodyPart)
        tail = bodyParts[len(bodyParts)-1]
    elif snake == snakeHead:
        global snakebodyParts
        global stail
        snakebodyPart= t.Turtle(shape="circle")
        snakebodyPart.speed(0)
        snakebodyPart.penup()
        snakebodyParts.append(snakebodyPart) 
        stail = snakebodyParts[len(snakebodyParts)-1]

def changeColor(snake): # Mod for 10,11
    snake.color(random(),random(),random())

def move():
    #Movement for player 1
    if head.direction == "up":
        head.sety(head.ycor()+20)
    elif head.direction == "down":
        head.sety(head.ycor()-20)
    elif head.direction == "left":
        head.setx(head.xcor()-20)
    elif head.direction == "right":
        head.setx(head.xcor()+20)
    #Movement for player 2
    if snakeHead.direction == "up":
        snakeHead.sety(snakeHead.ycor()+20)
    elif snakeHead.direction == "down":
        snakeHead.sety(snakeHead.ycor()-20)
    elif snakeHead.direction == "left":
        snakeHead.setx(snakeHead.xcor()-20)
    elif snakeHead.direction == "right":
        snakeHead.setx(snakeHead.xcor()+20)

#Set Direction

#mod for 5
def up():
    if head.direction != "down" and not paused:
        head.direction="up"
        head.setheading(dup)
def down():
    if head.direction != "up" and not paused:
        head.direction="down"
        head.setheading(ddown)
def right():
    if head.direction != "left" and not paused:
        head.direction="right"
        head.setheading(dright)
def left():
    if head.direction != "right" and not paused:
        head.direction="left"
        head.setheading(dleft)

def upa():
    if snakeHead.direction != "down" and not paused:
        snakeHead.direction="up"
        snakeHead.setheading(dup)
def downa():
    if snakeHead.direction != "up" and not paused:
        snakeHead.direction="down"
        snakeHead.setheading(ddown)
def righta():
    if snakeHead.direction != "left" and not paused:
        snakeHead.direction="right"
        snakeHead.setheading(dright)
def lefta():
    if snakeHead.direction != "right" and not paused:
        snakeHead.direction="left"
        snakeHead.setheading(dleft)

def checkEdge(snake):
    if snake.ycor()>290 or snake.ycor()<-290 or snake.xcor()>290 or snake.xcor()<-290:
        hideTheBody(snake)

def checkFood(snake):
        if (abs(snake.xcor()-food.xcor()) <=19) and (abs(snake.ycor()-food.ycor()) <=19):
            # mod for  1
            global speed
            speed *= .1
            food.teleport(randint(-290,290),randint(-290,290))
            addPart(snake)
            changeColor(snake)

def moveBodyPart(snake):
    if snake == head:
        global tail
        for i in range(len(bodyParts)-1,0,-1):
            newX= bodyParts[i-1].xcor()
            newY= bodyParts[i-1].ycor()
            bodyParts[i].teleport(newX,newY)
            changeColor(bodyParts[i])
            if len(bodyParts)>0:
                newX = head.xcor()
                newY = head.ycor()
                neck = bodyParts[0]
                neck.teleport(newX,newY)
                bodyParts[max(-2,len(bodyParts)*-1)].shape("square")
                tail = bodyParts[max(len(bodyParts)-1,0)]
                tail.shape("triangle")
                #mod for 9 (Set tail direction to the opposite of where the snake is heading)
                match head.direction:
                    case "up":
                        tail.setheading(ddown)
                    case "down":
                        tail.setheading(dup)
                    case "left":
                        tail.setheading(dright)
                    case "right":
                        tail.setheading(dleft)
    elif snake == snakeHead:
        global stail
        for i in range(len(snakebodyParts)-1,0,-1):
            snewX= snakebodyParts[i-1].xcor()
            snewY= snakebodyParts[i-1].ycor()
            snakebodyParts[i].teleport(snewX,snewY)
            changeColor(snakebodyParts[i])
        if len(snakebodyParts)>0:
            snewX = snakeHead.xcor()
            snewY = snakeHead.ycor()
            sneck = snakebodyParts[0]
            sneck.teleport(snewX,snewY)
            snakebodyParts[max(-2,len(snakebodyParts)*-1)].shape("square")
            stail = snakebodyParts[max(len(snakebodyParts)-1, 0)]
            stail.shape("triangle")
            #mod for 9 (Set tail direction to the opposite of where the snake is heading)
            match snakeHead.direction:
                case "up":
                    stail.setheading(ddown)
                case "down":
                    stail.setheading(dup)
                case "left":
                    stail.setheading(dright)
                case "right":
                    stail.setheading(dleft)
#Mod for  4
def pause():
    global paused
    paused = not paused

#Check for inputs

wn.onkeypress(upa,"w")
wn.onkeypress(downa,"s")
wn.onkeypress(lefta,"a")
wn.onkeypress(righta,"d")
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(pause,"p")

#mod for 7
print(
f'''
Use p to pause

Player 1 Movement:
W For Up
A For Left
S For Down
D For Right

Player 2 Movement:

Arrow keys
'''

)

#Game Loop
wn.listen()
while True:
    if paused:
        time.sleep(.05)
        wn.update()
    while not paused:
        wn.update()
        time.sleep(delay)
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
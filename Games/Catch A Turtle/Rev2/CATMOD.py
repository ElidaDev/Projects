import turtle as t
import time
from random import randint

playing = True
wn=t.Screen()
wn.bgcolor("black")
wn.screensize(300,300)

scoreKeep=t.Turtle()
scoreKeep.teleport(250,350)
scoreKeep.color("white")
scoreKeep.ht()
scoreKeep.setx()
accuracyKeep = t.Turtle()
accuracyKeep.teleport(0,350)
accuracyKeep.color("white")
accuracyKeep.ht()
accuracyKeep.showturtle
timeKeep=t.Turtle()
timeKeep.teleport(-250,350)
timeKeep.color("white")
timeKeep.ht()
timer = 30

turtle =t.Turtle("turtle")
turtle.shapesize(2)
turtle.color("aquamarine")
turtle.speed(5)
score=0
def gameOver():
    global playing
    playing = False
def moveTurtle():
    turtle.goto(randint(-290,290),randint(-290,290))
def updateScore():
    global score
    score+=1
    scoreKeep.clear()
    scoreKeep.write(score, font=("Times New Roman",30,"normal"))
def hit(x,y):
    global timer
    global hits
    hits += 1
    timer += .5
    print("Whacked!")
    moveTurtle()
    updateTime()
    updateScore()
def updateTime():
        global timer
        timer = max(timer,0)
        if timer == 0:
            gameOver()
        timeKeep.clear()
        timeKeep.write(timer, font=("Times New Roman",30,"normal"))
def miss():
    global misses
    misses += 1
def updateAccuracy():
     global misses
     global hits
     accuracy = hits/max(misses,1)

turtle.onclick(hit)
wn.onclick(miss)
while playing:
    time.sleep(.5)
    timer -= .5
    updateTime()
wn.mainloop()
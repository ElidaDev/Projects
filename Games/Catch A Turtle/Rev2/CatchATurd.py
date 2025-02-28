import turtle as t
import time
import random as r
import Leaderboard as lb

#---global var and objects and game configuration
clicks = 0
hits = 0
wn = t.Screen()   #everything is clickable...
wn.bgcolor("black")
wn.setup(600,725)
points = ((-5, 0), (0, 10), (5, 0), (0, -10))
wn.register_shape("star", points)

turtle = t.Turtle(shape="turtle")
turtle.shapesize(2)
turtle.color("aquamarine")
turtle.speed(0)

scoreKeeper = t.Turtle()
scoreKeeper.speed(0)
scoreKeeper.teleport(300,315)
scoreKeeper.color("pink")
scoreKeeper.ht()

accuracyKeep = t.Turtle()
accuracyKeep.teleport(0,315)
accuracyKeep.color("white")
accuracyKeep.ht()


leaderBoardDrawer = t.Turtle()
leaderBoardDrawer.speed(0)
leaderBoardDrawer.teleport(-100,315)
leaderBoardDrawer.color("red")
leaderBoardDrawer.shape("star")
leaderBoardDrawer.ht()

timeKeeper = t.Turtle()
timeKeeper.color("goldenrod3")
timeKeeper.teleport(-300,315)
timeKeeper.ht()

welcomeTurt = t.Turtle()
welcomeTurt.color("green")
welcomeTurt.teleport(300,350)
welcomeTurt.write("Click the turtle to start!")
score=0
playing = True
starting = True
originalSize = 3
size = originalSize
timer=5
interval=500
fontSetup = ("Times New Roman", 30, "normal")

#---f(x)
#every command that is based on a mouse click MUST HAVE the x,y var passed in


def moveturtle():
    welcomeTurt.ht()
    global size
    global originalSize
    global playing
    playing= True
    flashScreen()
    turtle.color("red")
    turtle.stamp()
    turtle.color("aquamarine")
    newX=r.randint(-290,290)
    newY=r.randint(-290,290)
    turtle.goto(newX,newY)
    if size > ((originalSize/2)/2)/2:
        size /= 2
        turtle.shapesize(1*size,1*size)
    else:
        size = originalSize
        turtle.shapesize(1*size,1*size)

def updateScore():
    global score
    score+=1
    print(score)
    scoreKeeper.clear()   #clears ANYTHING it wrote..........................
    scoreKeeper.write(f"Score: {score}",font=("Times New Roman",30,"normal"))

def manageLeaderBoard(): #gameover/update HS
    global score
    highScorer = False
    if score > int(lb.getScores()[-1]):
        playerName = input("Congratulations, you made the LeaderBoard, Please enter a name: ")
        lb.updateLeaderboard(lb.getNames(),lb.getScores(),playerName,score)
        highScorer = True
    lb.drawLeaderboard(highScorer,lb.getNames(),lb.getScores(),leaderBoardDrawer,score)

def updateTimer():
    global playing
    if playing:
        global timer
        timer-= .5
        timeKeeper.clear()
    if timer<=0 and playing:
        playing = False
        #timeKeeper.write("Time's Up!",font=fontSetup)
        manageLeaderBoard()
    else:
        timeKeeper.write(f"Time: {timer}",font=fontSetup)
        timeKeeper.getscreen().ontimer(updateTimer,interval)

def flashScreen():
    wn.bgpic("")
    wn.bgcolor("red")
    time.sleep(0.25)
    wn.bgcolor("white")
    wn.bgpic("background.gif")

buffer = 15
def click(mouseX,mouseY):  #add any features to this f(x) that trigger when turtle is clicked
    global clicks
    clicks +=1
    if playing:
        if (mouseX >= turtle.xcor()-buffer and mouseX <= turtle.xcor()+buffer) and (mouseY>= turtle.ycor()-buffer and mouseY <= turtle.ycor()+buffer):
            global timer
            global hits
            hits += 1
            timer += .5
            print("Whacked!")
            moveturtle()
            updateScore()
        updateAccuracy()
        
def updateAccuracy():
    if playing:
        global clicks
        global hits
        global accuracy
        calculation = (hits/max(clicks,1))
        accuracy = round(min((calculation*100),100),2)
        accuracyKeep.clear()
        accuracyKeep.write(f"Accuracy: {accuracy}%",font= fontSetup)


#---events - event handlers
wn.onscreenclick(click)
wn.ontimer(updateTimer,interval)
wn.listen()
#---mainloop
wn.mainloop()

'''
    Features List:
        1. Click a turd
        2. Turd move randomly
        3. Score
        4. Timer
        5. High Score rev1 or tomorrow
'''

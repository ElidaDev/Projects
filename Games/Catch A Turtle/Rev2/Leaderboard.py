# set the levels of scoring

'''
Name requirements:
No ','
3 characters
UpperCase
'''
size = 2

# return names in the leaderboard file
def getNames(fileName = 'db.txt'):
    leaderboardFile = open(fileName, "r")  # be sure you have created this

    # use a for loop to iterate through the content of the file, one line at a time
    # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
    names = []
    for eachLine in leaderboardFile:
        leaderName = ""
        index = 0

        # DONE 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")
        while(eachLine[index] != ','):
            char = eachLine[index]
            leaderName += char
            index +=1

        # DONE 2: add the player name to the names list
        names.append(leaderName)
    leaderboardFile.close()

    #  DONE 6: return the names list in place of the empty list
    return names


# return scores from the leaderboard file
def getScores(fileName="db.txt"):
    leaderboardFile = open(fileName, "r")  # be sure you have created this

    scores = []
    for eachLine in leaderboardFile:
        leaderScore = ""
        index = 0

        # TODO 3: use a while loop to index beyond the comma, skipping the player's name
        while(eachLine[index] !=","):
            index+=1
        # TODO 4: use a while loop to get the score
        index +=1
        while(eachLine[index]!="\n"):
            char = eachLine[index]
            leaderScore+=char
            index += 1
        # TODO 5: add the player score to the scores list
        scores.append(leaderScore)
    leaderboardFile.close()

    # Done 7: return the scores in place of the empty list
    return scores


# update leaderboard by inserting the current player and score to the list at the correct position
def updateLeaderboard(leaderNames, leaderScores, playerName, playerScore, fileName="db.txt"):
    #Fix PlayerName To all caps
    playerName = playerName.upper()

    index = 0
    # TODO 8: loop through all the scores in the existing leaderboard list
    for eachScore in leaderScores:
        if int(playerScore)>int(eachScore) :
            break
        else:
            index +=1
    # TODO 10: insert new player and score
    leaderNames.insert(index,playerName)
    leaderScores.insert(index,str(playerScore))

    # TODO 11: keep both lists at 5 elements only (top 5 players)
    while len(leaderNames) > 5:
        leaderNames.pop()
        leaderScores.pop()
    # TODO 12: store the latest leaderboard back in the file
    leaderboardFile = open(fileName,"w")
    for i in range(5):
        leaderboardFile.write(leaderNames[i] + "," + str(leaderScores[i]) + "\n")
    leaderboardFile.close()
    '''
    
      # this mode opens the file and erases its contents for a fresh start

    # TODO 13 loop through all the leaderboard elements and write them to the the file
    for :
        leaderboardFile.write(leaderNames[index] + "," + str(leaderScores[index]) + "\n")

    leaderboardFile.close()
    '''

def newLine(turtleObject):
    turtleObject.penup()
    turtleObject.goto(-160, int(turtleObject.ycor()) - 50)
    turtleObject.pendown()

def drawMedal(color,turtleObject):
    turtleObject.showturtle()
    turtleObject.penup()
    turtleObject.sety(int(turtleObject.ycor())+50)
    turtleObject.setx(int(turtleObject.xcor())-25)
    turtleObject.color(color)
    turtleObject.stamp()
    turtleObject.setx(int(turtleObject.xcor())+25)
    turtleObject.sety(int(turtleObject.ycor())-50)
    turtleObject.pendown()
    turtleObject.ht()
# draw leaderboard and display a message to player
def drawLeaderboard(highScorer, leaderNames, leaderScores, turtleObject, playerScore):

    # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
    fontSetup = ("ComicSans", 20, "normal")
    turtleObject.clear()
    turtleObject.penup()
    turtleObject.goto(-200, 75)
    turtleObject.hideturtle()
    turtleObject.down()
    turtleObject.color("blue")
    turtleObject.write("---Leader Board---",font = fontSetup)
    newLine(turtleObject)
    newLine(turtleObject)
    # TODO 14: loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
    for i in range(len(leaderNames)):
        match i:
            case 0:
                drawMedal("gold",turtleObject)
            case 1:
                drawMedal("silver",turtleObject)
            case 2:
                drawMedal((.59,.30,0),turtleObject)
        turtleObject.color("lime")
        turtleObject.write(f"\n{i+1}.{leaderNames[i]}: {leaderScores[i]}\n",font = fontSetup)
        newLine(turtleObject)
    newLine(turtleObject)

    # TODO 15: display message about player making/not making leaderboard
    if highScorer:
        turtleObject.write("Congratulations!\nYou made the leaderboard!", font=fontSetup)
    else:
        turtleObject.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=fontSetup)
    '''

    '''

    # move turtle to a new line
    newLine(turtleObject)

    # TODO 16: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
    '''
     turtleObject.write("You earned a gold medal!", font=fontSetup)
     turtleObject.write("You earned a silver medal!", font=fontSetup)
     turtleObject.write("You earned a bronze medal!", font=fontSetup)
    '''   

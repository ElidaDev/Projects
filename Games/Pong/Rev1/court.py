import turtle


COURTHEIGHT = 600
COURTWIDTH = 1000

def drawCourt():
    cdraw = turtle.Turtle(shape="turtle",visible=False)
    cdraw.color("white")
    cdraw.pensize(2)
    cdraw.speed(0)
    
    cdraw.teleport(COURTWIDTH/2*-1 , COURTHEIGHT/2)
    cdraw.setheading(0)
    cdraw.pendown()
    cdraw.fd(COURTWIDTH)
    cdraw.teleport(cdraw.xcor(), COURTHEIGHT/2*-1)
    cdraw.bk(COURTWIDTH)
    cdraw.teleport(0,COURTHEIGHT/2*-1)
    cdraw.setheading(90)
    for i in range(COURTHEIGHT//50):
        cdraw.pd()
        cdraw.fd(26)
        cdraw.penup()
        cdraw.fd(26)

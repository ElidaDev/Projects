import ball as b
import turtle as t
import court as c

wn = t.Screen()
wn.register_shape("Diamond",((0, 0), (10, 10), (20, 0), (10, -10)))
wn.setup(width=1.0,height=1.0)
# wn.onkeypress(b.resetBall,"r")
wn.onkeypress(lambda: b.up(b.leftPlayer),"w")
wn.onkeypress(lambda: b.down(b.leftPlayer),"s")
wn.onkeypress(lambda: b.up(b.leftPlayer),"Up")
wn.onkeypress(lambda: b.down(b.leftPlayer),"Down")
wn.onkeypress(lambda: b.reset(), "space")
b.ball.shape("Diamond")
b.updateScores()
c.drawCourt()
b.moveBall()
b.resetBall()
#Foreshadowing is a narrative device used as a warning or indication of (a future event).
wn.listen()
wn.mainloop()

import time
import turtle
import math
import random
import pyglet


print ("\nRED TURTLE = THIEF\nBLUE TURTLE = POLICE\n\nPOLICE HAS TO CATCH THIEF AS SOON AS POSSIBLE\nBOTH THIEF AND POLICE CAN TAKE BOOST(GREEN CIRCLE) TO INCREASE THEIR SPEED\n\nCONTROLS:\nTHIEF- LEFT ARROW KEY TO TURN 22.5 DEGREE LEFT & RIGHT ARROW KEY TO TURN 22.5 DEGREE RIGHT\nPOLICE- a TO TURN 22.5 DEGREE LEFT & d TO TURN 22.5 DEGREE RIGHT\n")
pres=input("PRESS ENTER TO START")



start = time.time()
w=turtle.Screen()
w.setup(width = 1.0, height = 1.0)
w.title("CATCH THE THIEF")
w.bgcolor('orange')

snd = pyglet.media.load('music1.mp3')
looper = pyglet.media.SourceGroup(snd.audio_format, None)
looper.loop = True
looper.queue(snd)
p = pyglet.media.Player()
p.queue(looper)
p.play()

b=turtle.Turtle()
b.hideturtle()
b.penup()
b.speed(0)
b.color('black')
b.goto(670,365)
b.pensize(4)
b.pendown()
for side in range(2):
    b.right(90)
    b.forward(723)
    b. right(90)
    b.forward(1345)

redie=turtle.Turtle()
redie.color('red')
redie.shape('turtle')
redie.shapesize(1.1,1.1,1.1)
redie.penup()
redie.speed(0)
redie.setposition(random.randint(-670,670), random.randint(-365,365))
redie.left(90)

bluie=turtle.Turtle()
bluie.color('blue')
bluie.shape('turtle')
bluie.shapesize(1.1,1.1,1.1)
bluie.penup()
bluie.speed(0)
bluie.setposition(random.randint(-670,670), random.randint(-365,365))
bluie.left(90)

goal=turtle.Turtle()
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-670,670), random.randint(-365,365))
goal.color('green')
goal.shape('circle')

sp1=2
sp=2.5

def turnleft():
    redie.left(22.5)
    #redie.seth(180)

def turnright():
    redie.right(22.5)
    #redie.seth(0)

"""def turnup():
    redie.seth(90)

def turndown():
    redie.seth(270)
"""

def turnleft1():
    bluie.left(22.5)

def turnright1():
    bluie.right(22.5)

def iscollision(t1,t2):
    d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if d<15:
        return True
    else:
        return False

turtle.listen()
turtle.onkeypress(turnleft, "Left")
turtle.onkeypress(turnright, "Right")
#turtle.onkeypress(turnup, "Up")
#turtle.onkeypress(turndown, "Down")
turtle.onkeypress(turnleft1, "a")
turtle.onkeypress(turnright1, "d")

while True:
    redie.forward(sp)
    bluie.forward(sp1)
    if redie.xcor()>=670:
        swap=redie.ycor()
        redie.goto(-670,swap)
    elif redie.xcor()<=-670:
        swap=redie.ycor()
        redie.goto(670,swap)
    elif redie.ycor()>=365:
        swap=redie.xcor()
        redie.goto(swap,-365)  
    elif redie.ycor()<=-365:
        swap=redie.xcor()
        redie.goto(swap,365)
  
    if bluie.xcor()>=670:
        swap1=bluie.ycor()
        bluie.goto(-670,swap1)
    elif bluie.xcor()<=-670:
        swap1=bluie.ycor()
        bluie.goto(670,swap1)
    elif bluie.ycor()>=365:
        swap1=bluie.xcor()
        bluie.goto(swap1,-365)  
    elif bluie.ycor()<=-365:
        swap1=bluie.xcor()
        bluie.goto(swap1,365)  

    if iscollision(redie,goal):
        sound = pyglet.media.load('eat1.mp3', streaming=False)
        sound.play()
        goal.setposition(random.randint(-670,670), random.randint(-365,365))
        sp=sp+0.25

    if iscollision(bluie,goal):
        sound = pyglet.media.load('eat1.mp3', streaming=False)
        sound.play()
        goal.setposition(random.randint(-670,670), random.randint(-365,365))
        sp1=sp1+0.25
        
    df=math.sqrt(math.pow(redie.xcor()-bluie.xcor(),2)+math.pow(redie.ycor()-bluie.ycor(),2))  
    if df<15:    
        sound = pyglet.media.load('siren1.mp3', streaming=False)
        sound.play()
        time.sleep(4)
        break

end = time.time()
final=end-start
print("\nCAUGHT IN %.2f SECONDS" % round(final,2))
#turtle.done()        

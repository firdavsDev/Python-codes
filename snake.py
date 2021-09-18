import turtle
import time
import random

#qalinligi
w=500
h=500
ilon_cell=20
ovqat=20
ilon_tana=20

#vaqt
DELAY=200

#boshqaruv
def kuchish():
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x=ilon.xcor()
        y=ilon.ycor()
        segments[0].goto(x,y)


    if ilon.direction=="up":
        ilon.sety(ilon.ycor() + ilon_cell)
    elif ilon.direction=='right':
        ilon.setx(ilon.xcor() + ilon_cell)
    elif ilon.direction=='down':
        ilon.sety(ilon.ycor() - ilon_cell)
    elif ilon.direction=='left':
        ilon.setx(ilon.xcor() - ilon_cell)

def check_food():
    if ilon.distance(food)<ilon_cell:
        
        x=random.randint(-w/2+ovqat,w/2-ovqat)
        y=random.randint(-h/2+ovqat,h/2-ovqat)
        food.speed(0)
        food.goto(x,y)
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        colors=random.choice(['red','blue','white'])
        segment.color(colors)
        segment.penup()
        segments.append(segment)  
        segment.speed(0) 

def go_up():
    if ilon.direction!="down":
        ilon.direction='up'

def go_right():
    if ilon.direction!="left":
        ilon.direction='right'

def go_down():
    if ilon.direction!="up":
        ilon.direction='down'

def go_left():
    if ilon.direction!="right":
        ilon.direction='left'

def play():
    kuchish()
    check_food()
    oyna.update()
    turtle.ontimer(play,DELAY)

def stop():
    if ilon.xcor()>=300 or ilon.xcor()<=-300 or ilon.ycor()>=300 or ilon.ycor()<=-300:
        time.sleep(1)
        ilon.goto(0,0)
        play()
    

#oyna ochamiz
oyna=turtle.Screen()

#oyna chegarasi
oyna.setup(500,500)
#oyna nomi
oyna.title("Snake uyini")
#orqafont
oyna.bgcolor("green")

oyna.tracer(0)

#chiziq
chegara=turtle.Turtle()
chegara.color("red")
chegara.speed(0)
chegara.hideturtle()
chegara.pensize(5)
chegara.up()
chegara.goto(300,300)
chegara.down()
chegara.goto(300,-300)
chegara.goto(-300,-300)
chegara.goto(-300,300)
chegara.goto(300,300)


#tugma
oyna.listen()
oyna.onkey(go_up,"Up")
oyna.onkey(go_right,"Right")
oyna.onkey(go_down,"Down")
oyna.onkey(go_left,"Left")

#ilon
ilon=turtle.Turtle()
ilon.color('brown')
ilon.speed(0)
ilon.shape('square')
ilon.penup()
ilon.goto(0,0)

#ovqat
food=turtle.Turtle()
food.shape("circle")
colorss=random.choice(['red','blue','yellow'])
food.color(colorss)
food.shapesize(ovqat/ilon_tana)
food.penup()

#lets go
segments=[]
ilon.direction = 'up'
play()
stop()
turtle.done()
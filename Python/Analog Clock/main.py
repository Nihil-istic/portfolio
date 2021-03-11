#Import Modules
import time
import turtle

WIDTH, HEIGHT = 440, 440

#Set a Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(WIDTH, HEIGHT)
wn.tracer(0)

#Set a Turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

#def a Clock
def draw_clock(h, m, s, pen):
    
    #Set the circle
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color("white")
    pen.pendown()
    pen.circle(210)

    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    pen.color("lightblue")
    
    #Set the minute lines
    for _ in range(60):
        pen.fd(200)
        pen.pendown()
        pen.fd(10)
        pen.penup()
        pen.goto(0,0)
        pen.rt(6)
    pen.color("white")
    
    #Set the hour lines
    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    #Set the hours hand
    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(60)

    #Set the minutes hand
    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(120)

    #Set the seconds hand
    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

while True:
    #Get the current time
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    #Set a clock in the screen title
    timeupdate = "Time"+": "+time.strftime("%I")+":"+time.strftime("%M")+":"+time.strftime("%S")
    wn.title(timeupdate)

    #Draw the clock
    draw_clock(h, m, s, pen)

    wn.update()

    #Delay for 1 second
    time.sleep(1)

    pen.clear()



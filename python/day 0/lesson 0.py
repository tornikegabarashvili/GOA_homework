from turtle import *

#we want to paint the house

#step one: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square


#draw a door

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)     #width of the door
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()

color("red")
begin_fill
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()         #we took pen up because we need to paint the window
goto(10,130)    #first window coordinats
pendown()

color("brown")

begin_fill()
left(30)       #now we paint the first window
left(180)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


penup()         #we took pen up because we need to paint second window
goto(190,130)
pendown()

begin_fill()
forward(50)     #now we paint the window
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()



exitonclick()
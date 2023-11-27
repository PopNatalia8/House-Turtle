from turtle import *


setup(1000, 700)
title('House')
bgcolor('#64D6F4')  # a shade of blue for the background
speed(0)
pensize(5)

# Creating the grass

color('#86DC3D')
penup()
goto(-500, -100)
pendown()
begin_fill()
for i in range(2):
    forward(1000)
    right(90)
    forward(250)
    right(90)
end_fill()

# Creating the sun

penup()
goto(-350, 200)
color('#FFF700')
pendown()
begin_fill()
circle(40)
end_fill()

# Creating the clouds


def cloud(x, y):
    penup()
    goto(x, y)
    color('white')
    pendown()
    begin_fill()
    forward(200)
    left(45)
    circle(20, 200)
    right(160)
    circle(30, 150)
    right(160)
    circle(40, 200)
    right(160)
    circle(20, 200)
    right(170)
    circle(15, 215)
    forward(10)
    end_fill()


cloud(-200, 150)
cloud(200, 100)

# Fence


def fence(a, b):
    penup()
    goto(a, b)
    color('#7B3F0D')
    fillcolor('#A0522D')
    pendown()
    begin_fill()
    forward(40)
    left(90)
    forward(150)
    left(60)
    forward(40)
    left(60)
    forward(40)
    left(60)
    forward(150)
    left(90)
    forward(40)
    end_fill()


fence(-468, -100)
fence(-395, -100)
fence(-322, -100)
fence(-249, -100)
fence(-176, -100)
fence(-103, -100)
fence(-30, -100)
fence(43, -100)
fence(116, -100)
fence(189, -100)
fence(262, -100)
fence(335, -100)
fence(408, -100)
fence(481, -100)

# Creating the house

penup()
goto(0, -150)
color('#CC99FF')
pendown()
begin_fill()
for _ in range(2):
    forward(300)
    left(90)
    forward(250)
    left(90)
end_fill()

# Creating the roof

penup()
goto(0, 100)
color('#A52A2a')
pendown()
begin_fill()
forward(300)
left(140)
forward(200)
left(80)
forward(200)
left(140)
end_fill()

# door of the house

penup()
goto(130, -150)
color('black')
pendown()
begin_fill()
for _ in range(2):
    forward(40)
    left(90)
    forward(50)
    left(90)
end_fill()

# Window1

penup()
goto(30, 0)
color('grey')
penup()
begin_fill()
for _ in range(2):
    forward(50)
    right(90)
    forward(50)
    right(90)
end_fill()

# Window2

penup()
goto(270, 0)
color('grey')
penup()
begin_fill()
for _ in range(2):
    back(50)
    left(90)
    back(50)
    left(90)
end_fill()

# Tree

penup()
goto(-250, -20)
color('#704214')
pendown()
begin_fill()
for _ in range(2):
    forward(40)
    right(90)
    forward(130)
    right(90)
end_fill()

# Tree crown
penup()
forward(20)
begin_fill()
color('#03AC13')
circle(80)
end_fill()

# birds


def bird(x, y):
    penup()
    goto(x, y)
    color('black')
    pendown()
    circle(20, 90)
    setheading(300)
    circle(20, 90)


bird(300, 300)
bird(320, 220)
bird(400, 250)


def grass(x, y):
    penup()
    goto(x, y)
    color('#C5E908')
    pendown()
    setheading(180)
    circle(30, 60)
    setheading(120)
    circle(30, 60)


grass(-400, -300)
grass(-300, -200)
grass(-200, -300)
grass(-400, -150)
grass(-100, -210)
grass(0, -250)
grass(400, -300)
grass(300, -200)
grass(200, -320)
grass(400, -150)
grass(100, -200)


hideturtle()
exitonclick()

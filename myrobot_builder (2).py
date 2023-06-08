import turtle as t 

def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('fastest')
t.bgcolor('seashell')

#feet
t.goto(-100, -150)
rectangle(50,20,'black')
t.goto(-30,-150)
rectangle(50,20,'black')

#legs
t.goto(-25, -50)
rectangle(25,100,'purple')
t.goto(-55,-50)
rectangle(-25,100,'purple')

#body
t.goto(-90,100)
rectangle(100,150,'blue')

#arms
t.goto(-150, 70)
rectangle(60,15,'grey')
t.goto(-150,70)
rectangle(15,55,'grey')

t.goto(10, 70)
rectangle(60,15,'grey')
t.goto(55,110)
rectangle(15,40,'grey')

#neck
t.goto(-50,120)
rectangle(15,20,'grey')

#head
t.goto(-85,170)
rectangle(80,50,'gold')

#eyes
t.goto(-60, 160)
rectangle(30,10,'white')
t.goto(-55,155)
rectangle(5,5,'black')
t.goto(-40,155)
rectangle(5,5,'black')

#mouth
t.goto(-65,135)
rectangle(40,5,'black')

#cap
t.goto(-75,190)
rectangle(60,20,'black')

#bag
t.goto(-170,20)
rectangle(50,5,'red')
t.goto(-170,20)
rectangle(5,20,'red')
t.goto(-120,20)
rectangle(5,20,'red')
t.goto(-185,5)
rectangle(85,40,'red')
t.hideturtle()

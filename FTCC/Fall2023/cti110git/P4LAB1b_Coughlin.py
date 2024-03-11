import turtle
win = turtle.Screen()
t = turtle.Turtle()

#options
t.pensize(2)

#moving to start point
t.penup()
t.setpos(-100, 100)
#drawing H
t.setheading(270)
t.pendown()
t.forward(100)
#moving to middle
t.sety(50)
#cross
t.setheading(0)
t.forward(35)
#second line
t.setpos(-65, 100)
t.setheading(270)
t.forward(100)

#move to start R
t.penup()
t.setpos(-55, 0)
#drawing R
t.setheading(90)
t.pendown()
t.forward(100)
#semicircle of R
t.setheading(0)
t.circle(-25, 180)
#R leg
t.setheading(305)
t.setposition(-30, 0)

#move to start of C
t.penup()
t.setpos(15, 90)
#drawing C
#topcurve
t.setheading(120)
t.pendown()
t.circle(20, 155)
#wall
t.setheading(270)
t.forward(57)
#bottomcurve
t.circle(20, 175)



win.mainloop()

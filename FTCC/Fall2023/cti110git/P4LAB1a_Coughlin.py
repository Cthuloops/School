import turtle
win = turtle.Screen()
t = turtle.Turtle()

#shapes
shapes = ['square', 'triangle']

#shape dicts
shape_sides = {'square':4, 'triangle':3}
shape_angles = {'square':90, 'triangle':120}

for shape in shapes:
    sides_drawn = 0
    while sides_drawn < shape_sides[shape]:
        t.forward(90)
        t.left(shape_angles[shape])
        sides_drawn += 1

win.mainloop()

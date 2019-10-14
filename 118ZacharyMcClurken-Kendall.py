import turtle as trtl

pm = trtl.Turtle()
pm.speed(0)

wn = trtl.Screen()

startx = 0
starty = 0

for i in range(9): # Put all of this in a loop once you got code finished

    # Make Pacman's body
    pm.setheading(0)
    pm.pensize(1.5)
    pm.goto(startx, starty)
    pm.fillcolor("yellow")
    pm.begin_fill()
    pm.circle(30)
    pm.end_fill()
    pm.penup()

    # Make Pacman's mouth
    pm.goto(startx + 21, starty + 10)
    pm.pendown()
    pm.setheading(135)
    pm.fillcolor("black")
    pm.begin_fill()
    pm.forward(30)
    pm.right(90)
    pm.forward(30)
    pm.penup()
    pm.forward(30)
    pm.right(90)
    pm.forward(40)
    pm.end_fill()

    # Make Pacman's eye
    pm.penup()
    pm.goto(startx + 2.5, starty + 45)
    pm.pendown()
    pm.fillcolor("black")
    pm.begin_fill()
    pm.circle(3)
    pm.end_fill()
    pm.penup()

    # Make pellet 1
    if i < 2:
        pm.goto(30, 40)
        pm.right(90)
        pm.pendown()
        pm.fillcolor("white")
        pm.begin_fill()
        pm.circle(10, 360, 4)
        pm.end_fill()
        pm.penup()
    # Make pellet 2
    if i < 3:
        pm.goto(60, 30)
        pm.pendown()
        pm.fillcolor("white")
        pm.begin_fill()
        pm.circle(10, 360, 4)
        pm.end_fill()
        pm.penup()
    # Make pellet 3
    if i < 5:
        pm.goto(90, 30)
        pm.pendown()
        pm.fillcolor("white")
        pm.begin_fill()
        pm.circle(10, 360, 4)
        pm.end_fill()
        pm.penup()

    # Make the power pellet
    if i < 6:
        pm.goto(120, 30)
        pm.pendown()
        pm.fillcolor("lightgoldenrodyellow")
        pm.begin_fill()
        pm.circle(10)
        pm.end_fill()
        pm.penup()

    
    if i < 7:
        # Make the ghost
        pm.goto(190, 0)
        pm.setheading(0)
        pm.fillcolor("red")
        pm.begin_fill()
        pm.circle(30)
        pm.end_fill()
        pm.penup()

        # Make the ghost's left
        pm.goto(180, 30)
        pm.pendown()
        pm.fillcolor("white")
        pm.begin_fill()
        pm.circle(8)
        pm.end_fill()
        pm.penup()

        # Make the right eye
        pm.goto(210, 30)
        pm.pendown()
        pm.fillcolor("white")
        pm.begin_fill()
        pm.circle(8)
        pm.end_fill()
        pm.penup()

        # Make the left pupil
        pm.goto(185, 33)
        pm.pendown()
        pm.fillcolor("blue")
        pm.begin_fill()
        pm.circle(5)
        pm.end_fill()
        pm.penup()

        # Make the right pupil
        pm.goto(215, 33)
        pm.pendown()
        pm.fillcolor("blue")
        pm.begin_fill()
        pm.circle(5)
        pm.end_fill()
        pm.penup()
    else: # Make the ghost blue
        pm.goto(190, 0)
        pm.setheading(0)
        pm.fillcolor("blue")
        pm.begin_fill()
        pm.circle(30)
        pm.end_fill()
        pm.penup()

        # Make the left eye completely white
        pm.goto(180, 30)
        pm.pendown()
        pm.fillcolor("white")
        pm.begin_fill()
        pm.circle(8)
        pm.end_fill()
        pm.penup()

        # Make the right eye completely white
        pm.goto(210, 30)
        pm.pendown()
        pm.fillcolor("white")
        pm.begin_fill()
        pm.circle(8)
        pm.end_fill()
        pm.penup()
        
        # Make the ghost mouth and make it white
        pm.goto(180,15)
        pm.setheading(0)
        pm.fillcolor("white")
        pm.begin_fill()
        pm.forward(25)
        pm.right(90)
        pm.forward(8) 
        pm.right(90)
        pm.forward(25)
        pm.right(90)
        pm.forward(8) 
        pm.end_fill()


    startx += 20
    

    wn.bgcolor("black")
    pm.clear()



wn.mainloop()

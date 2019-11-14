import turtle
bob = turtle.Turtle()
angle = 7.5
bob.speed(0)

def part(distance):
    bob.pendown()
    bob.begin_fill()
    bob.forward(100/distance)
    bob.left(85)
    bob.forward(150/distance)
    bob.left(95)
    bob.forward(125/distance)
    bob.left(95)
    bob.forward(150/distance)
    bob.end_fill()
    bob.left(90)
    bob.color("yellow")
    bob.begin_fill()
    for times in range(180):
        bob.forward(1.305/distance)
        bob.left(1)
    bob.forward(1/distance)
    bob.left(90)
    bob.forward(150/distance)
    bob.forward(1/distance)
    bob.end_fill()
    bob.penup()
    bob.color("black")
    bob.left(90)
    bob.forward(100/distance)
    bob.pendown()
    bob.left(80)
    bob.color("blue")
    bob.begin_fill()
    bob.forward(142/distance)
    bob.right(90)
    for times in range(180):
        bob.forward(1.305/distance)
        bob.right(1)
    bob.forward(1/distance)
    bob.end_fill()
    bob.left(180)
    bob.color("black")
    bob.penup()

def part2(distance):
    bob.color("black")
    bob.pendown()
    bob.begin_fill()
    bob.forward(100/distance)
    bob.right(85)
    bob.forward(150/distance)
    bob.right(95)
    bob.forward(125/distance)
    bob.right(95)
    bob.forward(150/distance)
    bob.right(90)
    bob.end_fill()
    bob.color("yellow")
    bob.begin_fill()
    for times in range(180):
        bob.forward(1.305/distance)
        bob.right(1)
    bob.forward(1/distance)
    bob.right(90)
    bob.forward(150/distance)
    bob.forward(1/distance)
    bob.end_fill()
    bob.penup()
    bob.color("black")
    bob.right(90)
    bob.forward(100/distance)
    bob.pendown()
    bob.right(80)
    bob.color("blue")
    bob.begin_fill()
    bob.forward(142/distance)
    bob.left(90)
    for times in range(180):
        bob.forward(1.305/distance)
        bob.left(1)
    bob.forward(1/distance)
    bob.end_fill()
    bob.right(180)
    bob.color("black")
    bob.penup()
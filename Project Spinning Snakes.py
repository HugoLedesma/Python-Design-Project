from ProjectFile import*

bob.penup()
bob.goto(-300,-280)
for times in range(18):
    part2(2)
    bob.left(angle)
    bob.penup()
    bob.forward(50)
    bob.pendown()
    bob.left(angle)

bob.penup()
bob.goto(300,280)
for times in range(18):
    part(2)
    bob.right(angle)
    bob.penup()
    bob.forward(50)
    bob.pendown()
    bob.right(angle)

bob.penup()
bob.goto(-25,280)
bob.pendown()
for times in range(18):
    part(2)
    bob.right(angle)
    bob.penup()
    bob.forward(50)
    bob.pendown()
    bob.right(angle)

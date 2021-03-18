import turtle

screenr=turtle.Screen()
pointer = turtle.Turtle()

def h1():
    pointer.sety(pointer.ycor()+10)
def h2():
    pointer.sety(pointer.ycor()-10)
def h3():
    pointer.sety(pointer.forward(10))
def h4():
    pointer.sety(pointer.back(10))

screenr.onkey(h1,'Up')
screenr.onkey(h2,'Down')
screenr.onkey(h3,'Right')
screenr.onkey(h4,'Left')

screenr.listen()
turtle.mainloop()

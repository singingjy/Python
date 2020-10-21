import turtle as t

def turn_right():
    te.setheading(0)
def turn_up():
    te.setheading(90)
def turn_left():
    te.setheading(180)
def turn_down():
    te.setheading(270)
def space():
    te.forward(100)




te = t.Turtle()
te.shape("turtle")
te.color("green")
te.forward(100)
te.setheading(90)
te.forward(100)
te.setheading(180)
te.forward(100)
te.setheading(270)
te.forward(100)

te.up()
te.goto(0,200)

te.left(90)
te.down()
for x in range(3): #repeat
      te.forward(100)
      te.left(120)
#거북이 움직이게 하는 코드
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(space,"space")
t.listen() 


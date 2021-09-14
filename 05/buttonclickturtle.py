import turtle as t


def turtle_forward():
    t.forward(50)
    t.stamp()
def turtle_leftward():
    t.left(90)
    t.forward(50)
    t.stamp()
def turtle_backward():
    t.backward(50)
    t.stamp()
def turtle_rightward():
    t.right(90)
    t.forward(50)
    t.stamp()
def restart():
    t.reset()

t.shape('turtle')
t.stamp()
t.onkey(turtle_forward,'w')
t.onkey(turtle_leftward,'a')
t.onkey(turtle_backward,'s')
t.onkey(turtle_rightward,'d')
t.onkey(restart, 'Escape')
t.listen()

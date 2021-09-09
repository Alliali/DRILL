import turtle as t

t.speed(5)
count = 5
while (count >= 0):
    t.forward(500)
    t.penup()
    t.backward(500)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.pendown()
    count-=1
t.penup() 
t.home()
t.pendown()
t.left(90)
cnt = 5
while (cnt >= 0):
    t.forward(500)
    t.penup()
    t.backward(500)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.pendown()
    cnt-=1

t.exitonclick()

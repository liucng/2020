"""import turtle as t

t.setup(700,500,100,200)
t.pu()
t.fd(-150)
t.pd()
t.pencolor("purple")
t.seth(-40)
t.bk(60)
t.pensize(5)
for i in range(4):
    t.circle(40,80)
    t.circle(-40,80)
#t.seth(0)
t.circle(40,80/2)
t.fd(40)
t.circle(5,180)
t.fd(40)

#t.circle()
t.done()
"""
import turtle as t

t.pu()
t.goto(-25, 50)
t.seth(90)
# t.fd(50)

t.pd()

for i in range(20):
    t.circle(30 - i, 360)
    t.width(3)
    # TODO: write code...
t.pu()
t.goto(25, 50)
t.pd()
t.pu()
t.seth(0)
t.left(90)
# t.fd(50)
t.pd()
for i in range(20):
    t.circle(-(30 - i), 360)
t.pu()
t.goto(150, 25)
t.pd()
t.pensize(6)
t.circle(150, 45)
for i in range(30):
    t.circle(-(30 - i), 360)
t.circle(150, 90)
for i in range(30):
    t.circle(-(30 - i), 360)
t.circle(150, 45)
# t.circle(150,180)
t.width(3)
t.pu()
t.goto(0, -25)
t.width(1)
t.pd()
t.circle(10, 180)
t.circle(10, -180)
t.circle(-10, 180)
t.pu()
t.goto(0, 0)
t.width(2)
t.pd()
t.seth(0)
for i in range(5):
    t.fd(5)
    t.circle(5 - i, 180)
    # t.fd(5)
    t.circle(5 - i, -180)
    # t.fd(-5)
    t.circle(6 - i, 180)
# t.goto(-7,-4)
t.pencolor("black")
t.done()
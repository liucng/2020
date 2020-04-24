"""
from turtle import*


setup(600,350,1,0)#设置窗体的大小（width,height,startx,starty),setup不是必须的
penup()
fd(-250)
pendown()
pensize(25)
colormode(255)
pencolor(25,255,255)#turtle.colormode(mode)-1.0:RGB小数值模式——255：RGB整数值模式
#pencolor("color")
seth(-40)#改变海归的行进角度，只改变方向但不行进 turtle.left(angle)
# turtle.seth(angle),angle为绝对角度                 turtle.right(angle)
for i in range(6):
    circle(40,80)
    circle(-4,80)
circle(40,80/2)
fd(40)
circle(16,180)
fd(40*2/3)
done()
"""
from turtle import*


#setup(600,350,10,0)#设置窗体的大小（width,height,startx,starty),setup不是必须的
penup()
fd(-25)
pendown()
pensize(2)
pencolor("blue")#turtle.colormode(mode)-1.0:RGB小数值模式——255：RGB整数值模式
seth(-36)#改变海归的行进角度，只改变方向但不行进 turtle.left(angle)
# turtle.seth(angle),angle为绝对角度                 turtle.right(angle)
for i in range(50):
    # TODO: write code...
    circle(-40,180)
    pencolor("red")
    circle(40,180)
    pencolor("blue")
    circle(-40,180)

done()
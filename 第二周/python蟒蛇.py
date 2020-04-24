import  turtle#第一种不会带来函数重名问题

#from turtle import*第二种会出现
#import <库名> as <库别名>给调用的外部库关联一个更短，更适合自己的名字
#<库名>.<库别名>(<函数参数>)
turtle.setup(600,350,1,0)#设置窗体的大小（width,height,startx,starty),setup不是必须的
turtle.penup()#turtle.pu()成对出现turtle.up()
turtle.fd(-250)
turtle.pendown()#turtle.pd()
#turtle.width(25)
turtle.pensize(25)#turtle.width(width)画笔宽度
turtle.pencolor("tomato")#颜色字符串
#RGB的小数值：turtle.pencolocr(0.22,0.2,0.1)
#RGB的元组值：turtle.pencolor((0.63,0.13,0.94))
#turtle.colormode(mode)-1.0:RGB小数值模式——255：RGB整数值模式
turtle.seth(-40)#改变海归的行进角度，只改变方向但不行进                turtle.left(angle)
# turtle.seth(angle),angle为绝对角度 turtle.setheading(angle)       turtle.right(angle)
for i in range(6):   #for<变量> in range(<参数>)---<变量>表示每次循环的次数,0到<次数>-1
    #range(N)产生0到N-1的整数序列，共N个，range（M,N）产生M到N-1的整数序列，共N-M个
    turtle.circle(40,80)
    turtle.circle(-4,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
"""turtle.fd(d)向海龟的正前方走turtle.forward(d)"""
"""turtle.bk(d)向海龟的后方走"""
"""turtle.circle(r,angle)以海龟的当前方向左侧某个点为圆心，当r为负的时候，圆心在右侧"""


#from <库名>import<函数名>
#from <库名>import*

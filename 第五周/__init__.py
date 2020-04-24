def <函数名>(<参数(0个或多个)>,[可选参数]):
    <函数体>
    return <返回值>可以有返回值，也可以没有

<函数名>(<参数>)调用是要给出实际的参数，实际参数替换定义的参数，调用后得到返回值

def <函数名>(<参数,*b >):
    < 函数体 >
    global s
    return < 返回值 >

n,s = 10,100
def fact(n):
    global s  #声明此处s为全局变量s
#fact(10,5)   (10,5)元组类型
ls = ["f","F"]#通过使用[]真实创建了一个全局变量列表ls
def func(a):
    #ls=[]此处ls是列表类型，真实创建，ls为局部变量
    ls.append(a)#此处ls是列表类型，未真实创建则等同于全局变量
    return
func("C")#全局变量被修改
print(ls)
#['f', 'F', 'C']

#lambda
#是匿名函数，使用lambda保留字定义，函数名是返回结果
#用于定义简单的、能够在一行内表示的函数
"""
<函数名> = lambda <参数>:<表达式>    
 等价于  def <>(<>):
            <>
            return <>

f =lambda x,y:x+y
f(10,15)
"""
f = lambda :"lambda"
print(f())
#lambda
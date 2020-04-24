#二分支结构
#紧凑形式：适用于简单表达式的二分支结构
'''<表达式1>if <条件>else<表达式2>'''
#guess = eval(input())
#print("猜{}了".format("对" if guess==1 else "错"))
"""x and y   与
x or y 或
not x 非"""
"""x = True
y = False
z = False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)"""



"""try:
   num = eval(input("整数："))
   print(num**2)
except :
   print("不是整数")
#except<异常类型>:  标注异常类型后，仅相应该异常 ，异常类型名字等同于变量
else:
    #<语句块3>      在不发生异常时执行
finally:
    #<语句块4>  无论是否发生异常，语句块4一定执行"""
"""try:
    num = eval(input(""))
except NameError:
    print()
"""

"""for i in range(12,0,-2):
    print(i)"""
"""for i in "1,2,3,4,5,6,7,8,9,abc,a,b,c":
    print(i,end="")"""
for line in fi:
    <语句块>
-fi是一个文件标识符，遍历每行，产生循环

while <条件>:
    <语句块>

break 跳出并结束当前整个循环，执行循环后的语句
continue 结束当前循环，继续执行后续次数循环


for <循环变量>   in <遍历结构>:
    <语句>
else:
    <语句>
#当循环没有被break语句退出时，执行else语句块
while <条件>:
    <语句块>
else:
    <语句块>


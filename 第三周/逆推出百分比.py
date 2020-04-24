"""dayup = float(input("输入百分比："))"""
"""i = pow(1.01,365)
z=0
for d in range(365):
    if d %7 in[0,6]:
        x = i/0.99
        z+=1
    else:
        x = i/x
        #i=x^(365-weekend)*(1-0.01)^(weekend)

"""
def dayup(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = (1 - 0.01)*dayup
        else:
            dayup = (1 + df) * dayup
    return dayup
dayfactor=0.01
while dayup(dayfactor)<37.78:
    dayfactor+=0.001

print("{:.3f}".format(dayfactor))

"""
def greetPerson(*name):
    print('Hello', name)
  
greetPerson('Runoob', 'Google')


Hello ('Runoob', 'Google')
加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数"""


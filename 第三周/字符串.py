"""print("'字符'")
print('"字符"')
print('''字符(')(")''')"""
a=["1","2",3,4]
b=["1","2",'3',"4",5]
c="零一二三四五六"
var1 = 'Hello World!'
var2 = "Runoob"

print("var1[0]: ", var1[0])#var1[0]:  H
print("var2[1:5]: ", var2[1:5])#var2[1:5]:  unoo
print("a[0:1]:",a[0:1])#a[0:1]: ['1']
print("a",a[0:3])#a ['1', '2', 3]
print("a[0:]:",a[0:])#a[0:]: ['1', '2', 3, 4]
print("b[:-1]:",b[:-1])#b[:-1]: ['1', '2', '3', '4']
print("b[:-2]:",b[:-2])#b[:-2]: ['1', '2', '3']
print("b",b)#b ['1', '2', '3', '4', 5]
print("b[2]:",b[2])#b[2]: 3
print("c[:3]:",c[:3])#c[:3]: 零一二
print("var1[0:8:2]:",var1[0:8:2])#var1[0:8:2]: HloW
print("c:",c[::-1])#c: 六五四三二一零
print("c:",c[::-3])#c: 六三零
print("c[::1]:",c[::1])#零一二三四五六
#转义符\---表达特定字符的本意
#print("这里有个双引号(\")")
#"\b"回退   "\n"换行   "\r"回车   "\t"制表符
#x+y 连接两个字符串
#n*x或x*n  复制n次字符串x
#x in s 如果x是s的子串，返回true,否则false
#len(x)  长度，返回字符串x的长度
#len("一二三四567")
#结果： 7
"""
str(x)  任意类型的x所对应的字符串形式
str(1.23)结果为"1.23",str([1,23])结果为"[1,23]"
 hex(x)或oct(x)整数x的十六进制或八进制的小写字符串
 0x1c8   0o710
 chr(u)  u为Unicode编码，返回其对应的字符
 "1+1=2"+chr(10004)   '1+1=2✔'
 ord(x)  x为字符，返回其对应的Unicode编码
 chr(9801)    ord('♉')
 chr(9800)
Out[10]: '♈'
for i in range(12):
     print(chr(9800+i),end="")   
♈♉♊♋♌♍♎♏♐♑♒♓
"""

"""str.lower()或str.upper()返回字符串的副本，全部字符小写或大写
"ABCDEFG".lower()    'abcdefg'

str.split(sep=None) 返回一个列表，由str根据sep被分割部分组成
"asd".split(",")  "a,sd".split(",")
['asd']             ['a', 'sd']

str.count(sub)  返回子串sub在str中出现的次数
"aAa s a BNB CXZ".count("a")    Out[17]: 3

str.replace(old,new)  返回字符串str副本，所以old子串被替换为new
"python".replace("n","n123.io")     Out[18]: 'python123.io'

str.center(width[,fillchar])  字符串str根据宽度width居中，fillchar可选
"abcd".center(10,"-")       Out[19]: '---abcd---'

str.strip(chars)  从str 中去掉在其左侧和右侧中列出的字符
"= python=".strip('" =np")  结果为"ytho"  "abcde".strip("ae")  Out[22]: 'bcd'

str.join(iter)在iter变量除最后元素外每个元素后增加一个str
",".join("12356")
Out[24]: '1,2,3,5,6'
主要由于字符串分割等"""


"""x = True
y = False
z = False

if x or y and z:
    print("yes")
else:
    print("no")
and 拥有更高优先级，会先行运算
x = True
y = False
z = False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)
    优先级顺序为 NOT、AND、OR
    
"""
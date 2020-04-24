weekStr ='星期一星期二星期三星期四星期五星期六星期天'
weekid = eval(input("输入希望获得的星期（1-7）："))
if weekid in [1,2,3,4,5,6,7]:
    print("今天是星期"+weekStr[((3*weekid)-1):((weekid*3)):1])
else:
    print("false")
"""WeekStr = '一二三四五六天'
Weekid = eval(input("输入希望获得的星期（1-7）："))
if Weekid in [1,2,3,4,5,6,7]:
    print("星期"+WeekStr[(Weekid-1):Weekid])
else:
    print("false")
"""
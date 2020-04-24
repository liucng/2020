import datetime
import time
t1=time.time()
t2=time.strftime("%Y-%m-%d %H:%M:%S")
date = datetime.datetime.now()
t3=datetime.datetime.fromtimestamp(t1)
print(t1,"\n"+t2)
print(date,t3)
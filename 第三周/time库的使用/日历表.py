import time as t
start=t.perf_counter()
date = t.strftime("%Y-%m-%d")
print(date)
#ti=t.strptime(date,"%Y-%m-%d")
#print(ti)
end=t.perf_counter()
e=end-start
print("{0:.2e}".format(e))


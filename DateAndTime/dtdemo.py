import time, datetime

epochseconds =time.time()
print(epochseconds)
9
t = time.ctime(epochseconds)
print(t)
dt = datetime.datetime.today()
print(dt)
print(dt.day,dt.month,dt.year)
print(dt.hour,dt.min,dt.second)





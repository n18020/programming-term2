from datetime import datetime

time = datetime.now()
print(time)

data = list(map(lambda x : x, range(1,1000000)))

time_2 = datetime.now()
print(time_2)

print(time_2 - time)


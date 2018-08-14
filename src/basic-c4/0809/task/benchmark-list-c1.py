from datetime import datetime

time = datetime.now()
print(time)

data = []
for i in range(1, 1000000):
    data.append(i)

time_2 = datetime.now()
print(time_2)

print(time_2 - time)

from random import *

index = 0
# customers = range(1,51)
customers = []
customers = list(customers)

while index < 50:
    customers.append(randrange(5,51))
    index += 1

print(customers)

count = 0
index = 0
for customer in customers:
    if customer >= 5 and customer <= 15:
        print('[O]{index}번째 손님 (소요시간 : {time}분)'.format(index = index, time = customer))
        count += 1
    else:
        print('[ ]{index}번째 손님 (소요시간 : {time}분)'.format(index = index, time = customer))

    index += 1

print('총 탑승 승객 : {count}분'.format(count = count))
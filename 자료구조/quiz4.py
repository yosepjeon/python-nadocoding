from random import *

#lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
users = range(1,21)
users = list(users)

print("-- 당첨자 발표 --")
shuffle(users)
chicken = sample(users,1)
users.remove(chicken[0])
print("치킨 당첨자 : {chicken}".format(chicken=chicken[0]))

shuffle(users)
print("커피 당첨자 : {coffee}".format(coffee = sample(users,3)))

print("-- 축하합니다 --")

# 해설답
users = range(1,21)
users = list(users)

print("-- 당첨자 발표 --")
shuffle(users)
winners = sample(users,4)
print("치킨 당첨자 : {chicken}".format(chicken=winners[0]))

shuffle(users)
print("커피 당첨자 : {coffee}".format(coffee = winners[1:]))

print("-- 축하합니다 --")

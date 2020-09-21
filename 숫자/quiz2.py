from random import *

print('####### random() 함수 사용 ######')
print(random())                 # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)            # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))       # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)   # 1 ~ 10 이하의 임의의 값 생성

print('###### randrange(n, m) ######')
print(randrange(1,46))          # 1 ~ 45 미만의 임의의 값 생성

print('###### randint(n,m) ######')
print(randint(1,45))            # 1~45 이하의 임의의 값 생성

print('###### Quiz ######')
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")

date = randrange(3,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")

date = int(random() * 28) + 4
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")

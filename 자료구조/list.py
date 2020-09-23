# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10,20,30]
print(subway)

subway = ['유재석','조세호','박명수']
print(subway)

# 조세호씨가 몇 번쨰 칸에 타고있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append('하하')
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

subway.append('유재석')
print(subway)
print(subway.count('유재석'))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ['조세호',20,True]

num_list.extend(mix_list)
print(num_list)

# cabinet = {3:'유재석',100:"김태호"}
# print(cabinet.get(3))
#
# # print(cabinet[5]) # Error 발생
# # print(cabinet.get(5)) # None 출력 후 로직 계속해서 수행
# # print(cabinet.get(5,"정준하"))
# # cabinet[5] = '정준하'
# print(cabinet)
#
# print(3 in cabinet)

cabinet = {'A-3':'유재석', 'B-100':'김태호'}
print(cabinet['A-3'])
print(cabinet['B-100'])

# 새 손님
print(cabinet)
cabinet['A-3'] = '김종국'
cabinet['C-20'] = '조세호'
print(cabinet)

# 간 손님
del cabinet['A-3']
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key,value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)
sentence = '나는 소년입니다'
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""

print(sentence3)

print('###### slicing #######')
jumin = "990120-1234567"
print('성별: ' + jumin[7])
print('연: ' + jumin[0:2]) # 0부터 2 직전까지 (0,1)
print("월: " + jumin[2:4])
print("일 " + jumin[4:6])

print('생년월일: ' + jumin[:6]) # 처음부터 6 직전까지
print('뒤 7자리: ' + jumin[7:]) # 7부터 끝까지
print('뒤 7자리 (뒤부터): ' + jumin[-7:]) # 맨뒤 -7번째부터 끝까지

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index('n')
print(index)
index = python.index('n',index+1)
print(index)

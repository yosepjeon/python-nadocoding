# import sys
# print('Python','Java', file=sys.stdout)
# print('Python','Java', file=sys.stderr)

# 시험 성적
# scores = {'수학':0,'영어':50,'코딩':100}
# for subject,score in scores.items(): # .items() (key,value) pair로 제공
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003 ...
# for num in range(1,21):
#     print('대기번호: ' + str(num).zfill(3))

answer = input('아무 값이나 입력하세요: ')
# 사용자 입력을 통해서 입력을 받게 되면 항상 문자열로 받는다.
print(type(answer))
print('입력하신 값은 ' + answer + '입니다.')
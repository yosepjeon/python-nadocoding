# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건: 파일명은 '1주차.txt', '2주차.txt',... 와 같이 만듭니다.
import os

def createReport(week):
    score_file = open('보고서/' + str(week) + '주차.txt', 'w', encoding='utf8')
    score_file.write('- {week} 주차 주간보고 -\n'.format(week=week))
    score_file.write('부서: \n')
    score_file.write('이름: \n')
    score_file.write('업무 요약: \n')

def createDirectory(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(OSError)
        # print('Error: creating directory. ' + path)

createDirectory("/Users/jeon-yoseb/PycharmProjects/project1/입출력/보고서")

index = 1
while index <= 50:
    createReport(index)
    index += 1

#  해답 코드
# for i in range(1,51):
#     with open(str(i) + "주차.txt","w",encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -\n".format(i))
#         report_file.write('부서: \n')
#         report_file.write('이름: \n')
#         report_file.write('업무 요약: \n')

from random import  *
# for waiting_no in [0,1,2,3,4]:
#     print('대기번호: {waiting_no}'.format(waiting_no = waiting_no))

# randrange()
# for waiting_no in range(1,6):
#     print('대기번호: {waiting_no}'.format(waiting_no=waiting_no))

# starbucks = ['아이언맨','토르','그루트']
# for customer in starbucks:
#     print('{customer}, 커피가 준비되었습니다.'.format(customer = customer))

# customers = ['아이언맨','토르','그루트']
# index = 3
# while index >= 1:
#     print('{customer}, 커피가 준비되었습니다.'.format(customer = customers[index-1]))
#     index -= 1

index = 0
while True:
    if index == 5:
        break;
    index += 1
    print(index)

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1,end='')
else:
    print(0,end='')
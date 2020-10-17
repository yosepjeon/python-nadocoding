A, B = map(int, input().split())

if A > B:
    print('>',end='')
elif A < B:
    print('<',end='')
else:
    print('==',end='')

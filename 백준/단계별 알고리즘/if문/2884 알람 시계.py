H, M = map(int, input().split())

N = int((15 + M) / 60) - 1
H = (H + N) % 24
M = (15 + M) % 60

print('{H} {M}'.format(H=H,M=M))
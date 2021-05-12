import sys

star = '*'
blank = ' '
N = int(sys.stdin.readline().rstrip())

for i in range(N,0,-1):
    count = ((N * 2) - (i * 2 - 1)) // 2
    print( blank*count + star*(i*2-1))
for i in range(2,N+1):
    count = ((N * 2) - (i * 2 - 1)) // 2
    print(blank*count + star*(i*2-1))
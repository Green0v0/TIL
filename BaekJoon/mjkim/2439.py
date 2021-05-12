import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    star = '*'
    blank = ' '
    print((blank*(N-1-i))+(star*(i+1)))

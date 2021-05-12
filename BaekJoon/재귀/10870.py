import sys
n = int(sys.stdin.readline().rstrip())
fibo = [0,1]
for i in range(2,n+1):
    fibo.append(fibo[i-2]+fibo[i-1])
print(fibo[n])
print(fibo.pop()) #아니 이거 왜 틀리냐; 어이업네
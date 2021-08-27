"""
8
0 1 0 1 0 0 0 1
2
1 3
2 3
1 남 : 스위치 받은 수 배수 상태바꿈 3 -> 3 6
2 여 : 양쪽을 기준으로 같으면 바꾸거 아님 본인숫자만
"""

import sys
def rev(number):
    if number == 0:
        return 1
    else:
        return 0
n = int(sys.stdin.readline())
switch = [-1] + list(map(int, sys.stdin.readline().split()))
students = int(sys.stdin.readline())

for _ in range(students):
    s, num = map(int, sys.stdin.readline().split())
    nn = num
    if s == 1: # 남자
        for k in range(nn, n+1, num):
            switch[k] = rev(switch[k])
    else: # 여자
        switch[nn] = rev(switch[nn])
        for k in range(n//2):
            if nn + k > n or nn - k < 0:
                break
            if switch[nn+k] == switch[nn-k]:
                switch[nn+k] = rev(switch[nn+k])
                switch[nn-k] = rev(switch[nn-k])
            else:
                break

# for i in range(0,len(switch),20):
#     print(*switch[i:i+20])
for i in range(1, n + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()

def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for i in range(num, N + 1, num):
            change(i)
    # 여자
    else:
        change(num)
        for k in range(N // 2):
            if num + k > N or num - k < 1: break
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break

for i in range(1, N + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()
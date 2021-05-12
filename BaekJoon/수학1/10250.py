import sys
T = int(sys.stdin.readline().rstrip())
li = []
for idx in range(T):
    H, W, N = map(int,sys.stdin.readline().split())
    key_W = N//H
    if N % H == 0: #배수일 때 0이 되어버린다.
        key_W = (N // H) - 1
    floor = N - (H * key_W)
    key_W += 1
    # 리스트를 넣거나 if로 10보다 작으면 0을 추가
    if key_W < 10:
        key_W = '0'+str(key_W)
        print(str(floor)+key_W)
        # li.append(str(floor)+key_W)
    else:
        print(str(floor)+str(key_W))
        # li.append(str(floor)+str(key_W))

# for i in range(T):
#     print(int(li[i]))

# 다른 풀이1
# N번째 손님 (N % H)*100 + N//H + 1 호에 머문다.

# 다른 풀이2
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    f = 0
    ho = 0
    if n % h == 0:
        f = h * 100
        ho = n // h
    else:
        f = (n % h) * 100
        ho = 1 + n // h
    print(f + ho)

# 밍두 풀이
t = int(input())
listT = []
for i in range(t):
    h, w, n = map(int, input().strip().split())
    temp_list = [h, w, n]
    listT.append(temp_list)

for i in listT:
    if i[2] % h == 0:
        # print(h)
        n_ho = i[2] // i[0]
        n_th = i[0]
    else:
        n_ho = i[2]//i[0]+1
        n_th = i[2]%i[0]
    print(n_th*100+n_ho)
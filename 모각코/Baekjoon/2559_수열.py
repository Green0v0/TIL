n, k = map(int, input().split())
li = list(map(int, input().split()))
l, r = 0, k
for i in range(n - k):
    if li[l] <= li[r]:
        l -= 1
        r += 1
    else:
        break
print(l,r)

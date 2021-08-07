li = list(map(int, input().split()))
odd = 0
even = 1
for i in li:
    if i % 2 == 0:
        even *= i
    else:
        if odd == 0:
            odd = 1
        odd *= i
if odd != 0:
    print(odd)
else:
    print(even)
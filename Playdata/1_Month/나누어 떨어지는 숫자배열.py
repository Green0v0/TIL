def solution(x):
    h = x
    sum_x = 0
    while h > 0:
        sum_x += h%10
        h = h//10
    if x%sum_x == 0:
        return True
    else:
        return False
# return n % sum([int(c) for c in str(n)]) == 0
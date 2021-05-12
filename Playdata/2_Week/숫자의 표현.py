# 15를 표현하는 연속적인 값의 합.
# 조건. 겹쳐도 고려한다.
# 조건. 대상 숫자도 포함된다.
# 효율성 실패
def solution(n):
    cnt = 0
    for i in range(n,0,-1):
        check = n
        start = i
        while start!=0:
            check = check-start
            if check == 0:
                cnt += 1
                break
            start-=1
    return cnt

# 포인터를 써보자
# 'ㅁ'b
def solution1(n):
    nlist = [x for x in range(n,-1,-1)]
    start = 0; end = start+1
    cnt = 0
    while True:
        if end>n:
            break
        total = sum(nlist[start:end])
        if total >= n:
            if total == n:
                cnt+=1
            start += 1
            end = start+1
        elif total < n:
            end+=1
    return cnt

# 다른 사람 풀이
# 첫 풀이와 차이점 파악하기
def solution2(num):
    answer = 0
    for i in range(1, num + 1):
        s = 0
        while s < num:
            s += i
            i += 1
        if s == num:
            answer += 1
    return answer

print(solution1(15))

# 다른 사람 풀이
# 예를 들어 n이 3개의 연속된 자연수(i-1, i, i+1)의 합으로 표현된다면 합은 3i가 됩니다.
# 즉, n은 3의 배수입니다.
# 마찬가지로 5개의 연속된 자연수의 합으로 n이 표현이 된다면 n은 5의 배수여야합니다.
# 따라서, n의 약수 중 홀수가 몇개있냐는 문제와 같은 문제로 해석할 수 있습니다.
def expressions(n):
    return len([i for i in range(1,n+1,2) if n % i is 0])
    # return len([i for i in range(1,n+1,2) if n % i == 0])
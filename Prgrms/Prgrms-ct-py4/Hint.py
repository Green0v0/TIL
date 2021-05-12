# 힌트를 참고하여 코드 작성
def solution(seat):
    answer = -1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer

# 가장 긴 팰린드롬
def solution(s):
    p = 0

    for i in range(len(s)):
        if s[i - p:i + 1] == s[i - p:i + 1][::-1]:
            p += 1
        elif i - p > 0 and s[i - p - 1:i + 1] == s[i - p - 1:i + 1][::-1]:
            p += 2

    return p

# 제가 문제 유형에 적은 것 처럼 이전 상태들을 통해 현재 값을 구할 수 있는지 판단하는 것이 중요합니다.
#
# ["ba","na","n","a"]와 "banana"로 예를 들어보면 "ba", "na"까지는 쉽게 체크가 가능합니다. 그래서 index가 3인 "a"까지는 count가 2입니다.
# 여기서 "banan"까지 오면 "n"이 존재하기 때문에 index가 4인 시점에 count가 3이됩니다.
# index가 5인 "banana"에서는 이전 상태가 "bana"와 "banan"이 두 개 존재합니다. "bana" 상태는 count가 2이고 "banan"은 count가 3입니다. "banan"에서 "banana"를 완성하면 count가 4가되고 "bana"에서 "banana"를 완성하면 count가 3이 되므로 더 작은 쪽을 선택하면 됩니다. 이런식으로 접근하면 DP적으로 접근에 성공했다고 볼 수 있습니다. :)
#
# 다음은 제가 작성한 코드입니다. 위 설명을 참고하며 한 번 확인해보세요!

# 단어 퍼즐
def solution(strs, t):
    dp = [0] * (len(t) + 1) # 미리 단어 길이만큼 리스트 생성합니다.

    strs = set(strs) # 리스트를 set으로 변환합니다.

    for i in range(1, len(t) + 1): # 편의를 위해 1부터 시작합니다.
        dp[i] = float('inf') # 처음엔 길이가 무한입니다. (조합이 불가능하다는 의미)
        for j in range(1, min(i + 1, 6)): # 단어 조각의 길이는 5 이하라는 점을 이용하여 루프를 돌립니다.
            start = i - j
            end = i
            if t[start:end] in strs: # 문자열 t의 start부터 end까지 strs에 포함되었는지 체크합니다.
                dp[i] = min(dp[i], dp[i - j] + 1) # 포함되었다면 현재값과 이전 값+1 중 더 작은 값을 저장합니다.

    return -1 if dp[-1] == float('inf') else dp[-1] # 최종 결과가 무한이라면 불가능하다는 뜻이니 -1을 반환합니다.



# 다른 사람 풀이
def solution1(m,n,puddles):
    grid = [[0]*(m+1) for i in range(n+1)] #왼쪽, 위로 한줄씩 만들어서 IndexError 방지
    if puddles != [[]]:                    #물이 잠긴 지역이 0일 수 있음
        for a, b in puddles:
            grid[b][a] = -1                #미리 -1로 체크
    grid[1][1] = 1
    for j in range(1,n+1):
        for k in range(1,m+1):
            if j == k == 1:                #(1,1)은 1로 만들어두고, 0이 되지 않도록
                continue
            if grid[j][k] == -1:           #웅덩이는 0으로 만들어 다음 덧셈 때 영향끼치지 않게
                grid[j][k] = 0
                continue
            grid[j][k] = (grid[j][k-1] + grid[j-1][k])%1000000007   #[a,b] = [a-1,b] + [a,b-1] 공식

    return grid[n][m]

def solution2(m, n, puddles):
    info = dict([((2, 1), 1), ((1, 2), 1)])
    for puddle in puddles:
        info[tuple(puddle)] = 0

    def func(m, n):
        if m < 1 or n < 1:
            return 0
        if (m, n) in info:
            return info[(m, n)]
        return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))
    return  func(m, n) % 1000000007
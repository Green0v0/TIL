# 작은 막대로 부수고 붙여 정확하게 x cm 막대
# 모든 막대 길이를 더한다(처음에는 64cm) 길이의 합이 x보다 크다면 다음을 반복
# 가장 짧은 막대를 반으로
# 두개 중 하나를 버려도 남아있는 막대들의 길이의 합이 x보다 크다면 하나를 버린다.
# 남아있는 막대들을 풀로 붙여 x cm로 생성
# 마지막 남은 막대들의 개수를 반환
# 만약 마지막 단계에서 막대가 하나밖에 없다면 1을 반환하라

# 이진수 활용 < 아닌듯ㅋㅋㅋㅋㅋㅋㅋㅋ
def solution(x):
    bar = [64, 32, 16, 8, 4, 2, 1]
    n = 0
    while True:
        if (x==0):
            return n
        for i in range(len(bar)):
            if (bar[i]<=x):
                x-=bar[i]
                n+=1
        return n

print(solution(65))
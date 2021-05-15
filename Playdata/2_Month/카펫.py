def solution(brown,yellow):
    # yellow의 약수들을 파악하기
    answer = []
    # 약수의 경우 sqrt까지 진행하면 된다!
    for i in range(1,int(yellow**0.5+2)):
        if yellow%i==0:
            j = yellow//i
            # 5*4  brown :14 yellow:6
            # if tab 확인
            # yellow**0.5까지 진행하면 j가 더 작은 값이라는 것이 고정됨.
            if brown == (j+2)*2+(i*2):
                answer = [j+2, i+2]
    # answer = sorted(answer,reverse=True)
    return answer
# print(solution(14,6))
print(solution(8,1))

def solution1(brown,yellow):
    # x=0;y=0
    xy = brown+4
    for i in range(1,brown+yellow+2):
        if (brown+yellow)%i == 0:
            pass
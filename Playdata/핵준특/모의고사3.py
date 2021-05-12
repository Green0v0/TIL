# 느낌표가 연속으로 여러개 -> 한개
# 느낌표와 물음표가 섞여 있다면 하나의 물음표로
# stack
def solution(document):
    # document = list(document.split())
    stack = []
    # ! ? 부분만 뽑아내기
    for i in document:
        if i == '!' or i == '?':
            stack.append(i)


print(solution("정말 그렇게 생각해요!!??"))
print(solution("정말 그렇게 생각해요!! 정말요?!"))
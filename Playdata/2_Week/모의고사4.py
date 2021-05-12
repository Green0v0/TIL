# ord 사용?
# code에 문자의 할당 index = 코드
# 메세지 <- 원본 or 암호 구분하여
def solution(code, message):
    answer = []
    if message.isdigit(): # 암호화된 메세지
        message = str(message)
        for i in range(0,len(message), 2):
            idx = int(message[i : i+2])
            answer.append(code[idx-1])
    else:
        for j in message:
            answer.append(str(code.find(j) + 1).zfill(2))
    print(answer)

    return ''.join(answer)

print(solution("abcdefghijklmnopqrstuvwxyz","20051920"))
# print(solution("abcedfghijklmnopqrstuvwxyz","testa"))


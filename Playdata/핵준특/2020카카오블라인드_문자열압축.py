# 완전탐색
# 1/2구간까지 모두 탐색!
def solution(s):
    # 가지치기
    if len(s) == 1:
        return 1
    # 10글자면 1,2,3,4,5
    cnt = 0
    result = ''
    min_s = float('inf')
    for i in range(1, len(s)//2 + 1):
        # 처음과 마지막을 필수로 체크하기
        check = s[:i] # 체크 초기화
        for j in range(i, len(s), i): # step을 i로
            target = s[j:j+i]
            if target == check:
                cnt += 1
            elif target != check:
                if cnt != 0:
                    result += ''.join([str(cnt+1),check])
                else:
                    result += ''.join(check)
                check = target
                cnt = 0

        if cnt != 0:
            result += ''.join([str(cnt+1),check])
        else:
            result += ''.join(check)

        min_s = min(len(result), min_s)
        result = '' # result 초기화
        cnt = 0 # cnt 초기화

    return min_s
    # print(result)
    # print(min_s)

print(solution('a'))

# 다른 사람 풀이 1
# words[1:] + [''] <- 이건 맨 마지막 처리를 따로 안빼고 같은 for문 안에서 해결하기 위해 추가한 코드
# [len(text)]의 경우 1자리수의 단어가 들어왔을 때를 처리해주기 위한 코드
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

# 리더님 코드
# 문자열이 1개일 경우는 answer = len(s)로 처리
# 굳이 문자열을 붙여보지 않고 다르면 숫자만 더하는 방식으로 진행
def solution(s):
    answer = len(s)

    for size in range(1, len(s) // 2 + 1):
        count = 1
        compress = 0

        prev = s[:size]
        for i in range(size, len(s) + size, size):
            curr = s[i:i + size]
            if prev == curr:
                count += 1
            else:
                compress += size + len(str(count)) if 1 < count else len(prev)
                prev = curr
                count = 1
        answer = min(answer, compress)

    return answer

# notion
# 문자열 자르기, 부분 문자열 얻기, 문자열 비교하기, 문자열 길이 얻기
def solution(s):
    answer = len(s)
    unit = 1
    while unit <= len(s)//2:
        comp = s[:unit]
        count = 1
        word = ""
        for i in range(unit, len(s), unit):
            if comp == s[i:i+unit]:
                count += 1
            else:
                if count == 1:
                    word += comp
                else:
                    word += str(count) + comp
                comp = s[i:i+unit]
                count = 1

        if count == 1:
            word += comp
        else:
            word += str(count) + comp

        unit += 1
        answer = min(answer, len(word))

    return answer
"""
아이디의 길이는 3~15
아이디는 소문자, 숫자, 빼기 `-`, 밑줄 `_`, 마침표 `.`
단, 마침표는 처음 & 끝에 사용 불가, 연속적으로 사용 불가

1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
"""
from collections import deque

def solution(new_id):
    dq = []
    # 소문자 치환
    new_id = new_id.lower()

    # 허용되는 문자열 외 제거
    for s in new_id:
        if not (s.isdigit() or s.isalpha() or s == '-' or s == '_' or s == '.'):
            # new_id.replace(s,'')
            continue
        # 4-1
        if len(dq) == 0 and s == '.':
            continue

        # '.'이 연속되는 경우 무시
        if len(dq) > 0 and dq[-1] == '.' and s == '.':
            continue

        dq.append(s)

    # 빈문자열인 경우 a 대입
    if len(dq) == 0:
        dq.append('a')

    # 16자 이상시 15될때까지 제거
    if len(dq) > 15:
        dq = dq[:15]
        if dq[-1] == '.':
            dq.pop()

    # 마지막에 . 있는 경우 제거
    if dq[-1] == '.':
        dq.pop()

    # 2자 이하시 길이가 3까지 같은 것 추가 반복
    if len(dq) < 3:
        new_dq = dq[-1]*(3 - len(dq))
        dq.append(new_dq)

    return "".join(dq)

print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution("z-+.^."	))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
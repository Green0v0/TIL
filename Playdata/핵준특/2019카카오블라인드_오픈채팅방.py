# 유저 아이디로 구분
# 아 이런 유형이 해시구나..! 저번 시험에도 이런 유형이 있었는데!
def solution(record):
    # 아이디 - 닉네임을 해시로 연결
    board = []
    do = {'Enter' : '님이 들어왔습니다.',
          'Leave' : '님이 나갔습니다.'}
    name = {}
    for r in record:
        rec = list(r.split())
        # print(rec)
        if rec[0] == 'Enter':
            name[rec[1]] = rec[2]
            board.append((rec[1],do[rec[0]]))
        elif rec[0] == 'Change':
            name[rec[1]] = rec[2]
        else:
            board.append((rec[1],do[rec[0]]))
    # [(id,명령어)]
    # print(board)
    # print(name)
    result = []
    for n, m in board:
        result.append(name[n]+m)

    return result

# print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

# notion
# 유저아이디에 대한 닉네임이 변경 -> 매핑 필요
# 변경 시, 과거 이력이 사라지고 전부 변경 -> 최종 닉네임
# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []
    user_dict = {}
    chatlog = []
    # format을 활용하여 끼워줄 것이다.
    enter_msg = '%s님이 들어왔습니다.'
    leave_msg = '%s님이 나갔습니다.'

    for rec in record:
        info = rec.split(" ")
        if info[0] == 'Enter':
            user_dict[info[1]] = info[2]
            chatlog.append([enter_msg, info[1]])
        elif info[0] == 'Leave':
            chatlog.append([leave_msg, info[1]])
        elif info[0] == 'Change':
            user_dict[info[1]] = info[2]

    # formatting
    for log in chatlog:
        answer.append(log[0] % user_dict[log[1]])

    # print(answer)
    return answer
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

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

print(answer)
# actions 명령어를 어떻게 처리할 것인가.
# action후 행동을 어떻게 정리해둘 것인가 dict 어떰
def solution(n, actions):
    board = dict()
    for x in range(1,n+1):
        board[str(x)] = board.get(str(x),[])

    for act in actions:
        # PUT i INSIDE j
        # SET i LOOSE
        # SWAP i WITH j
        # print(board)
        if "PUT" in act:
            i = act[4]
            j = act[-1]
            if i not in board.keys() or j not in board.keys():
                return -1
            board[j].append([i,board[i]])
            board.pop(i)
        elif "SET" in act:
            i = act[4]
            if i not in board.keys():
                return -1
            for k,v in board[i]:
                board[k] = board.get(k,v)
            board[i] = []
        elif "SWAP" in act:
            i = act[5]
            j = act[-1]
            if i not in board.keys() or j not in board.keys():
                return -1
            board[i], board[j] = board[j], board[i]
        print(board)
    # 가방 안이 가방 숫자보다 작아야함!
    b = [False]*n
    for key, value in board.items():
        b[int(key)-1] = True
        if value:
            # while value:
            #     idx, v = value.pop()
            #     if int(key) < int(idx):
            #         return -1
            # else:
            #     return len(board)
            zip_j = list(zip(*value))
            new = list(map(int,zip_j[0]))
            for z in new:
                b[z-1] = True
                if int(key) < z:
                    return -1
            if False in b and int(key) < b.index(False) + 1:
                return -1
    else:
        return len(board)


print(solution(4, ["PUT 3 INSIDE 2","SWAP 4 WITH 2","PUT 2 INSIDE 4","SET 1 LOOSE"]))
# solution(2, ["PUT 1 INSIDE 2","SET 2 LOOSE"])
print(solution(3, ["PUT 1 INSIDE 2","PUT 3 INSIDE 1"]))
print(solution(4,["PUT 1 INSIDE 2","PUT 2 INSIDE 4","PUT 3 INSIDE 4","SET 4 LOOSE"]))
# 끝말잇기
def solution(n, words):
    word = dict()
    last = ''
    for i in range(len(words)):
        word[words[i]] = word.get(words[i], 0) + 1
        if i != 0 and last != words[i][0]:
            answer = [(i % n) + 1,(i // n) + 1]
            break
        if word[words[i]] == 2:
            answer = [(i % n) + 1, (i // n) +1]
            break
        last = words[i][-1]
    else:
        return [0,0]

    return answer

# return [번호, 차례]
print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))
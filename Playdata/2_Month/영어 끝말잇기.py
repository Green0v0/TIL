def solution(n, words):
    dictionary = {}
    prev = ''
    cnt = 1
    for idx, value in enumerate(words):
        # 첫번째는 추가하고 끝
        if idx == 0:
            dictionary[value] = True
            prev = value
            continue

        if prev[-1] != value[0] or value in dictionary.keys():
            return [(idx%n)+1, cnt]

        dictionary[value] = True
        prev = value

        # cnt 관련 조건
        if idx%n == (n-1)%n:
            cnt += 1

    else:
        return [0,0]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2,["tank", "kick"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))
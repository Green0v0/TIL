import sys

# 중복되는 것 제거한 풀이 : 틀림 ㅠㅠ
word = sys.stdin.readline().split()
lower_word = list(map(lambda x: x.lower(),word))
lower_word = set(lower_word)
print(len(lower_word))

# 중복되는 것도 모두 세기
word = sys.stdin.readline().split()
print(len(word))
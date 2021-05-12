import sys

N = int(sys.stdin.readline().rstrip())
li_n = []
for i in range(N):
    li_n.append(sys.stdin.readline().rstrip())

def first_filter(word):
    list_word = list(word)
    set_word = set(list_word)
    if len(list_word) != len(set_word):
        return list_word
    else:
        return '1'

def second_filter(word):
    list_word = list(word)
    set_li = []
    total = 0
    for i in list_word:
        if list_word.count(i) > 1:
            set_li.append(i)
    set_li = set(set_li)
    # print(set_li)
    m = list(set_li)
    return m

def third_filter(word,m):
    list_word = list(word)
    total_list = []
    for midx in m :
        check = [i for i, j in enumerate(list_word) if j == midx]
        for idx in range(len(check),0,-1):
            try:
                if check[idx] - check[idx-1] > 1:
                    total_list.append(0)
                else:
                    total_list.append(1)
            except:
                pass
    return total_list

def fourth_filter(total_list):
    if total_list.count(0) > 0:
        return 0
    else:
        return 1

total = 0
for word in li_n:
    count = fourth_filter(third_filter(word,second_filter(first_filter(word))))
    total = total + count

print(total)

# 다른 풀이
a = int(input())
c = 0
for n in range(a):
  b = input()
  if list(b) == sorted(b,key=b.find):
    c += 1
print(c)

# 다른 풀이 2
N = int(input())
words = []
for i in range(N):
    words.append(input())
cnt = 0
for word in words:
    chars = [0]
    isGroupWord = 1
    for char in word:
        if char != chars[-1]:
            if char in chars: isGroupWord = 0
            else: chars.append(char)
    if isGroupWord: cnt += 1
print(cnt)
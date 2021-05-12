import sys
import string

alpha = list(string.ascii_uppercase)
S = sys.stdin.readline().rstrip()
list_s = list(S.upper())
alist = [0 for i in range(len(alpha))]

for a in range(len(alpha)):
    for s in range(len(list_s)):
        if alpha[a] == list_s[s]:
            alist[a] = alist[a] + 1

m = max(alist)
check = [i for i,j in enumerate(alist) if j==m]
if len(check) != 1:
    print('?')
else:
    print(alpha[alist.index(m)])

# 다른 풀이
word=input()
word=word.upper()

alpha_count_list=[0 for i in range(26)]

for s in word:
    list_idx=ord(s)-65
    alpha_count_list[list_idx]+=1

answer=max(alpha_count_list)

if alpha_count_list.count(answer)!=1:
    print("?")
else:
    answer_idx=alpha_count_list.index(answer)
    print(chr(answer_idx+65))

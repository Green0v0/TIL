# print(8+6+8+2+4+2+len(6))
import string
import sys

N = list(sys.stdin.readline().rstrip())
alpha = string.ascii_uppercase
list_al = list(alpha)
length = []

# print(len(alpha)) #26
for i in range(0,len(list(alpha))):
    i = i//3
    length.append(i)

# 예외처리
length[ord('S')-65] = 5
length[ord('V')-65] = 6
length[ord('Y')-65] = 7
length[ord('Z')-65] = 7

num = []
for idx in N:
    num.append(ord(idx)-65)

time = list(map(lambda x:length[x]+2,num))
# print(time)
total = 0
for i in time:
    total = total + i
print(total + len(time))

# 다른 풀이
a=[]
b=ord("A")
t=0
for n in range(8):
  if n==5 or n==7:
    a.append(list(map(chr,[b,b+1,b+2,b+3])))
    b+=4
  else:
    a.append(list(map(chr,[b,b+1,b+2])))
    b+=3
c=input()
for d in c:
  for f in enumerate(a):
    if d in f[1]:
      t+=(f[0]+3)
      break
print(t)

# 다른 풀이2
words = input().lower()
s = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

time = 0
for i in range(len(words)):
    for j in s:
        if(words[i] in j):
            time += s.index(j) + 3
print(time)
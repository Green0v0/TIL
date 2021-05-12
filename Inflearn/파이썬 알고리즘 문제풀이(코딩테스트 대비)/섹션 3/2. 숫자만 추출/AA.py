import sys
word = list(sys.stdin.readline().rstrip())
num = []
for i in range(len(word)):
    try :
        word[i] = int(word[i])
        num.append(str(word[i]))
    except:
        pass
a = ''
for i in num:
    a += i
a = int(a)
cnt = 0
for i in range(1,a+1):
    if a%i == 0:
        cnt+=1

print(a)
print(cnt)

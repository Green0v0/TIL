import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    word = list(sys.stdin.readline().rstrip().lower())
    for j in range(len(word)//2+1):
        if word[j] != word[len(word)-j-1]:
            result = 'NO'
            break
        else :
            result = 'YES'

    print(f'#{i+1} {result}')
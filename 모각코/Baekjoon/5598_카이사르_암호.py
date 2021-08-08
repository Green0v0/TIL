import sys
dic = {'A': 'X', 'B': 'Y', 'C': 'Z'}
st = sys.stdin.readline().rstrip()
result = ''
for s in st:
    if s in dic.keys():
        result += dic[s]
    else:
        result += chr(ord(s) - 3)
print(result)
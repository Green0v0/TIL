import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
h = int(sys.stdin.readline().rstrip())
li_h = []
for i in range(h):
    sample = int(sys.stdin.readline().rstrip())
    li_h.append(sample)
v = int(sys.stdin.readline().rstrip())
li_v = []
for i in range(v):
    sample = int(sys.stdin.readline().rstrip())
    li_v.append(sample)

try :
    # return
    final = (len(li_h)+1)*(len(li_v)+1)
    print(final)
except:
    pass
import sys
x,y,w,h = map(int,sys.stdin.readline().split())
li = [-(0-x),-(0-y),-(x-w),-(y-h)]
print(min(li))
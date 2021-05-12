import sys
while True:
    x,y,z = map(int,sys.stdin.readline().split())
    if x == 0 and y == 0 and z == 0:
        break
    sq = [x,y,z]
    sq = sorted(sq)
    if sq[2]**2 == sq[0]**2 +sq[1]**2:
        print('right')
    else:
        print('wrong')

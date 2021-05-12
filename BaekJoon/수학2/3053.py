import sys
import math
R = int(sys.stdin.readline().rstrip())
uclid = math.pi*(R**2)
Taxi = 2*(R**2)
print('{0:.6f}'.format(uclid))
print('{0:.6f}'.format(Taxi))
# 참고 사이트
# https://itholic.github.io/kata-taxicab-circle/
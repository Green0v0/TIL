# 가로 W, 세로 H
# math.gcd 최대 공약수
import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))
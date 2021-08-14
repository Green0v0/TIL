from collections import deque
import sys
"""나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
"""
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    t, idx = map(int, sys.stdin.readline().split())
    # 6 0
    imp = list(map(int, sys.stdin.readline().split()))
    m = max(imp)
    # if imp[idx] != m:
    # imp[idx] = (imp[idx], t)
    #
    # for item in imp:
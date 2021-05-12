# import string
#
# string.ascii_lowercase  소문자 abcdefghijklmnopqrstuvwxyz
# string.ascii_uppercase  대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_letters  대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits  숫자 0123456789

# 아스키 코드
# ord(문자) : 아스키 코드를 반환해준다
# chr(숫자) : 숫자에 맞는 아스키 코드를 반환한다

import string
import sys

alpha = list(string.ascii_lowercase)
N = sys.stdin.readline().rstrip()

for i in range(len(alpha)):
    qe = False
    for n in range(len(N)):
        if N[n] == alpha[i] :
            qe = True
            alpha[i] = n
    if qe == False:
        alpha[i] = -1

# 값만 나오게 하는 것
print(*alpha)

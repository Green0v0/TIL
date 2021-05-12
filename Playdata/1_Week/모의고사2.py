# 행운의 번호
# 가장 긴 행운의 번호의 길이
# -> 긴 번호 먼저 파악하기
def solution(s):
    # 우선 길이가 충분하지 않으면 제외
    # if len(s)<2:
    #     return 0
    answer = 0
    if len(s)%2!=0:
        length = len(s)-1
    else:
        length = len(s)
    for i in range(length,0,-2):
        # for j in range(0,length-i+1):
        for j in range(0,len(s)-i+1):
            # print(i,j)
            if sum(map(int,s[j:i//2+j])) == sum(map(int,s[i//2+j:i+j])):
                answer = i
                break
        if answer !=0:
            break
    return answer
    # else:
    #     return 0
print(solution('99999999'))

# 해설
class Solution:
    def solution(self, s):
        length = len(s)

        if length % 2 == 1:
            length -= 1

        while length > 0:
            cursor = 0
            while length + cursor <= len(s):
                sum_left = 0
                sum_right = 0
                for i in range(cursor, length / 2 + cursor):
                    sum_left += int(s[i])
                for i in range(length / 2 + cursor, length + cursor):
                    sum_right += int(s[i])
                if sum_left == sum_right:
                    return length
                cursor += 1
            length -= 2

        return 0

class Solution:
    def solution(self, s):
        answer = 0

        # 체크할 부분문자열의 첫 인덱스
        for i in range(len(s)):
            # 체크할 부분문자열의 마지막 인덱스
            for j in range(i + 1, len(s)):
                # 부분 문자열의 길이가 짝수일 때 확인,
                if (j - i) % 2:
                    s_part = s[i:j + 1]  # 인덱스 i부터 j까지
                    half = int((j - i + 1) / 2)
                    lft_s = s_part[:half]  # 왼쪽 부분
                    rgt_s = s_part[half:]  # 오른쪽 부분
                    sum_l = sum_r = 0  # 각각 왼쪽 부분의 숫자합, 오른쪽부분...

                    for k in range(len(lft_s)):
                        sum_l += int(lft_s[k])
                        sum_r += int(rgt_s[k])

                    # 만약 부분 문자열이 행운의번호라면 최대값으로 정답 업데이트
                    # 두 합이 같으면 행운의 번호
                    if sum_r == sum_l:
                        answer = max(answer, (j - i + 1))

        return answer


class Solution:
    def solution(self, s):
        self.s = s
        num = list(map(int, s))
        if len(s) % 2 != 0:
            max_len = len(s) - 1
        else:
            max_len = len(s)
        rng = int(max_len / 2)

        while True:
            for i in range(len(num)):
                try:
                    if num[2 * rng + i - 1] == False:
                        raise
                    if sum(num[i:rng + i]) == sum(num[i + rng:2 * rng + i]):
                        return 2 * rng
                except:
                    break
            rng -= 1
            if rng == 0:
                result = 0
            else:
                continue
        return result
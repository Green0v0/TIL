# 연속캐시
def solution(n,k,addresses):
    check = [i for i in range(k)]
    total = 0
    for i in addresses:
        min_ad = check[0]
        max_ad = check[-1]
        if i in check:
            continue
        if i > max_ad :
            if (i-max_ad)>=k:
                total += k
            else:
                total += (i-max_ad)
        elif i < min_ad:
            if (min_ad-i) >= k:
                total += k
            else:
                total += (min_ad-i)
        else:
            continue
        check = []
        cnt = k
        if i == 0:
            check = [z for z in range(k)]
            continue
        while cnt!=0:
            check.append(i-cnt+1)
            cnt-=1
    return total

solution(100,5,[6,0,3,20,22,16])
solution(100,999,[0,4,123,987,999,500,0])
solution(1,1,[0])

# 해설
class Solution:
    def solution(self, n, k, addresses):
        read = 0
        min = 0
        max = k - 1

        for i in addresses:
            # 읽어야 하는 캐시가 오른쪽에 있는 경우
            if i > max:
                if i - max > k:
                    read += k
                else:
                    read += (i - max)
                max = i
                min = i - (k - 1)
            # 읽어야 하는 캐시가 왼쪽에 있는 경우
            elif i < min:
                if min - i > k:
                    read += k
                else:
                    read += (min - i)
                max = i + (k - 1)
                min = i

        return read

class Solution:
    def solution(self, n, k, addresses):
        answer = 0
        now_bitrange = [0, k - 1]

        # 어드레스의 모든 요소 조회
        for i in addresses:
            # 현재 갖고 있는 바이트 범위를 벗어날 때
            if i > now_bitrange[1]:
                if i > now_bitrange[1] + k:
                    answer += k
                else:
                    answer += i - now_bitrange[1]
                now_bitrange[0] += i - now_bitrange[1]
                now_bitrange[1] = i
            elif i < now_bitrange[0]:
                if i < now_bitrange[0] - k:
                    answer += k
                else:
                    answer += now_bitrange[0] - i
                now_bitrange[1] -= now_bitrange[0] - i
                now_bitrange[0] = i

        return answer


class Solution:
    def solution(self, n, k, addresses):
        max_ad = k - 1
        min_ad = 0
        acc_count = 0

        for data in addresses:
            if min_ad <= data <= max_ad:
                continue
            else:
                if data > max_ad:
                    count = data - max_ad if data - max_ad < k else k
                    max_ad = data
                    min_ad = data - k + 1

                else:
                    count = min_ad - data if min_ad - data < k else k
                    max_ad = data + k - 1
                    min_ad = data

                acc_count += count

        return acc_count
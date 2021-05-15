# 가장 짧은 팰린드롬
def solution(s):
    word = s
    if s == s[::-1]:
        return len(s)
    for i in range(len(s)):
        word = word+s[i::-1]
        if word == word[::-1]:
            return len(word)
        word = s

print(solution('abab'))
print(solution('abacaba'))
print(solution('qwerty'))

# 해설
class Solution:
    def solution(self, s):

        not_in = []
        s_copy = list(s)
        s_desc = []
        for i in s_copy:
            s_desc.append(i)
        s_desc.reverse()

        # string s 내부의 팰린드롬 찾기
        while True:
            if s_copy == s_desc:
                break
            else:
                not_in.append(s_copy[0])
                del s_copy[0]
                s_desc = []
                for i in s_copy:
                    s_desc.append(i)
                s_desc.reverse()

        # 팰린드롬에 포함되지 않은 요소들 붙여 주기
        s_copy = list(s)
        not_in.reverse()
        s_copy += not_in

        length = len(s_copy)
        return length

class Solution:
    def solution(self, s):
        self.s = s
        x = self.s
        n = len(s)
        ans = 0

        for i in range(n):
            if x[i:] == x[i:][::-1]:
                ans = n + i
                break

        return ans
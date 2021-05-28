def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
            continue
        n1 = str(format(num, 'b'))
        n1 = '0' + n1
        n1 = list(n1)
        for i in range(len(n1) - 1, -1, -1):
            if n1[i] == '0':
                n1[i] = '1'
                n1[i + 1] = '0'
                break
        n2 = "".join(n1)
        n2 = int(n2, 2)
        answer.append(n2)
    return answer
    #     i = 0
    #     diff = float('inf')
    #     while diff != 2 and diff != 1:
    #         i += 1
    #         diff = bin(num^num+i)[-10:].count('1')
    #         # if diff == 2 or diff == 1:
    #         #     break
    #
    #     result.append(num+i)
    # return result

print(solution([2,7]))

# 다른 풀이
def solution(numbers):
    answer = []
    for number in numbers:
        if number & 1:
            target = number
            idx = 0
            while number > 0:
                if number % 2 == 0:
                    break
                number //= 2
                idx += 1
            answer.append(target + 2 ** (idx) - 2 ** (idx-1))
        else:
            answer.append(number+1)

    return answer
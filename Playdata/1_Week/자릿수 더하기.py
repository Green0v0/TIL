def solution(n):
    answer = 0
    while n != 0:
        answer += n%10
        n = n//10
    # if number < 10:
    #     return number;
    # return (number % 10) + sum_digit(number // 10)
    return answer
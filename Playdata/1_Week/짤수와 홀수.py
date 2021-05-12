def solution(num):
    answer = ''
    if num%2==0:
        answer='Even'
    else:
        answer='Odd'
    return "Even" if num%2 == 0 else "Odd"
    # return "Odd" if num%2 else "Even"
def solution(a, b):

    cnt_a = 0
    cnt = 0
    yoo = ['FRI','SAT','SUN','MON','TUE','WED','THU']

    for i in range(1,a+1):
        if i <= 7:
            if i % 2 == 1:
                if i == 1:
                    cnt = 0
                elif i == 3:
                    cnt = 29
                else:
                    cnt = 30
            else:
                cnt = 31
        else:
            if i % 2 == 0:
                if i == 8:
                    cnt = 31
                else:
                    cnt = 30
            else:
                cnt = 31
        cnt_a += cnt

    day = (cnt_a+b)%7

    return yoo[day-1]
# months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
# return days[(sum(months[:a-1])+b-1)%7]
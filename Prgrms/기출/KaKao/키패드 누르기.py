"""
1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
    4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
"""

def solution(numbers, hand):
    result = ''
    key = {1 : (0,0), 2: (1,0), 3:(2,0),
           4:(0,1), 5:(1,1), 6:(2,1),
           7:(0,2), 8:(1,2), 9:(2,2),
           '*':(0,3),0:(1,3),'#':(2,3)}
    left = '*'
    right = '#'

    for i in numbers:
        if i in (1, 4, 7):
            result += 'L'
            left = i
        elif i in (3, 6, 9):
            result += 'R'
            right = i
        else:
            # n = list(map(lambda x: abs(x[0] - x[1]), list(zip(a, b))))
            # point_i = key[i] # 5의 좌표
            # point_l = key[left]
            # point_r = key[right]
            l_i = sum(list(map(lambda x: abs(x[0]-x[1]), list(zip(key[i], key[left])))))
            r_i = sum(list(map(lambda x: abs(x[0]-x[1]), list(zip(key[i], key[right])))))
            if l_i < r_i or (l_i == r_i and hand == 'left'):
                result += 'L'
                left = i
            elif l_i > r_i or (l_i == r_i and hand == 'right'):
                result += 'R'
                right = i
            # else:
            #     if hand == 'left':
            #         result += 'L'
            #         left = i
            #     else:
            #         result += 'R'
            #         right = i
    return result

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")) #"LRLLLRLLRRL"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")) #"LLRLLRLLRL"

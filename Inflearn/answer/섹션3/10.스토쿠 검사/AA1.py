import sys
sudocu = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
# sudocu = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]

final = True
def row(x):
    check = list(range(1, 10))
    for j in x:
        try:
            for i in j:
                check.remove(i)
            else:
                return True
                # break
            # break
        except:
            return False
            # break
def col(x):
    check = list(range(1, 10))
    for i in range(len(x)):
        try:
            for j in range(len(x[i])):
                check.remove(x[i][j])
            else:
                return True
        except:
            return False

def block(sudocu):
    check = list(range(1,10))
    try:
        # 앞의 for 2개를 while로 변환
        x_start = 0
        y_start = 0
        while x_start > 9:
            print(x_start)
            while y_start > 9:
                print(y_start)
                # cnt = 0
                for x in range(3):
                    for y in range(3):
                        # y_start = j
                        check.remove(sudocu[x_start][y_start])
                        y_start+=1
                    x_start+=1
                    # cnt += 1
                    # if cnt == 3:
                    #     break
                y_start += 3
            x_start += 3
        return True

    except:
        return False
print(block(sudocu))
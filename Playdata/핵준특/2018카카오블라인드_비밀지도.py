def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        add = ''
        bin_or = str(bin(arr1[i] | arr2[i]))[2:]
        bin_or = bin_or.zfill(n)

        # bin_or = bin_or.replace('1', '#')
        # bin_or = bin_or.replace('0', ' ')
        # result.append(bin_or)

        for j in bin_or:
            if j == '1':
                add += '#'
            else:
                add += ' '
            # add += '#' if j == '1' else ' '

        result.append(add)

    return result

# print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))

# notion2
def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        final_line = str(bin(a1 | a2))[2:]
        final_line = '0'*(n - len(final_line)) + final_line
        final_line = final_line.replace('1', '#')
        final_line = final_line.replace('0', ' ')
        answer.append(final_line)

    return answer
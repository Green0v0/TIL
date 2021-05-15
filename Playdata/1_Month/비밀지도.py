def solution1(n,arr1,arr2):
    answer = []
    for i in range(len(arr1)):
        ground1 = ['0' for _ in range(n)]
        ground2 = ['0' for _ in range(n)]
        result = ['#' for _ in range(n)]
        bin_1 = list(bin(arr1[i])[2:])
        bin_2 = list(bin(arr2[i])[2:])
        for j in range(1, len(bin_1)+1):
            ground1[-j] = bin_1[-j]
        for x in range(1, len(bin_2)+1):
            ground2[-x] = bin_2[-x]
        for k in range(n):
            if ground1[k] == '0' and ground2[k] == '0':
                result[k] = ' '
        answer.append(result)
    final = []
    for z in answer:
        final.append(''.join(z))
    return final

# 다른 사람의 풀이
# bin(i|j) 2진수로 변환 후 or 연산자 적용
# rjust(width,[fillchar]) 원하는 문자를 따로 지정하여 다른 문자열로 앞 부분을 채워줄 수 있는 특징이 있다.
# zfill(width) -> "2".zfill(3) == "002"
def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
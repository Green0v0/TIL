def solution(arr1, arr2):
    # arr3=arr1
    # for i in range(len(arr1)):
    #     for j in range(len(arr1[0])):
    #         arr3[i][j] = arr1[i][j]+arr2[i][j]
    # answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    answer=[[sum(x) for x in list(zip(arr1[i],arr2[i]))] for i in range(len(arr1))]
    # for i in range(len(arr1)):
    #     answer.append([sum(x) for x in list(zip(arr1[i],arr2[i]))])
    return answer
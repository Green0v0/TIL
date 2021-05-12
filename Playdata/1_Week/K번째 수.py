def solution(array, commands):
    rearr=[]
    answer = []
    for co in commands:
        rearr = sorted(array[co[0]-1:co[1]])
        answer.append(rearr[co[2]-1])
    return answer
# return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
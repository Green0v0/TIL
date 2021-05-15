def solution(text):
    mtext = max(text, key= lambda x:len(x))
    print(mtext)
    answer = []
    for i in text:
        if i != mtext:
            answer.append(i.rjust(len(mtext)))
            continue
        answer.append(i)
    return answer
print(solution(["AAA","BBBBB","CCC"]))
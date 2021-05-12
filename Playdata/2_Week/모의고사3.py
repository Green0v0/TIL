def solution(sequence):
    sequence = sorted(sequence, key = lambda x:(len(x),x[0]))
    return sequence
print(solution(["1","174","23","578","71","9"]))
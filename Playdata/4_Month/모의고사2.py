# set 차집합 교집합
def solution(diet, breakfast, lunch):
    if set(list(breakfast)) & set(list(lunch)):
        return "CHEATER"

    br_la = set(list(breakfast)) | set(list(lunch))
    di = set(list(diet))
    result = sorted(list(di - br_la))
    if br_la - di:
        return "CHEATER"
    # result = list(di - br_la).sort()
    return "".join(result)

# 식단 Diet
# 저녁에 먹을 음식을 알파벳 순서로
# 식단에 없는 음식을 아침과 점심에 먹 or 식단보다 더 많이 먹으면 cheater(대문자)
# 식단에는 있지만 식단에 포함 된 횟수보다 더 많이 먹었을 경우??
# -> breakfast와 launch에 동시에 등장하는 음식은 없다며,,,
# 저녁에 먹을 음식을 알파벳 순서로 배열하여 리턴

print(solution("ABCD","AB","C")) #"D"
print(solution("ABEDCS","",""))
print(solution("EDSMB","MSD","A"))
print(solution("","",""))
def solution(s):
    if len(s)==4 or len(s)==6:
        return s.isdigit()
    else:
        return False
#     return s.isdigit() and len(s) in (4, 6)
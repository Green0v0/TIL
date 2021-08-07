# 백스페이스 -
# 화살표 < or >
L = int(input().rstrip())
for _ in range(L):
    cursor = 0 # 커서 idx
    sen = input().rstrip()
    all_s = ''

    for s in sen: # <<BP<A>>Cd-
        left, right = all_s[:cursor + 1], all_s[cursor + 1:]
        if s == '<':
            if cursor != 0:
                cursor += (-1)
            continue
        elif s == '>':
            cursor += 1
            continue
        # print(cursor)
        elif s == '-':
            left, right = all_s[:cursor+1], all_s[cursor+1:]
            all_s = left[:-1] + right
        else:
            if cursor == len(all_s):
                all_s += s
            left += s
            cursor += 1
    print(left+right)
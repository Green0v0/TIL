# 최솟값구하기
arr = [5,3,7,9,2,5,2,6]
# 최솟값을 저장할 변수 선언
arrMin=float('inf') # 파이썬에서 가장 큰 값으로 초기화
for i in range(len(arr)):
    if arr[i]<arrMin:
        # <= 과 < 차이는 순서도 고려할 때 차이를 둔다. <= 이면 뒤에 값으로 <는 더 빠른 인덱스로
        arrMin = arr[i]

print(arrMin)
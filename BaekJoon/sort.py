# 정렬할 변수
x = [3,6,2,8,1,4,9,10]

# 버블정렬 Bubble Sort
def bubble_swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubbleSort(x):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] > x[i+1]:
                bubble_swap(x, i , i+1)

# print(list(reversed(range(len(x)))))
# [7, 6, 5, 4, 3, 2, 1, 0]

# bubbleSort(x)

# 선택정렬 Selection Sort
def slection_swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def selectionSort(x):
    for size in reversed(range(len(x))):
        max_i = 0
        for i in range(1, 1+size):
            if x[i] > x[max_i]:
                max_i = i
        slection_swap(x, max_i, size)

# print(x)
# selectionSort(x)
# print(x)

# 삽입정렬 Insertion Sort


# 병합정렬
def mergeSort(x):
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]

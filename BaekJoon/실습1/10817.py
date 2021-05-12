a, b, c = map(int,input().split())
x = [a, b, c]

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubbleSort(x):
    for size in reversed(range(len(x))):
        for i in range(size) :
            if x[i] > x[i+1]:
                swap(x,i,i+1)

bubbleSort(x)
print(x[1])
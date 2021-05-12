h1 = int(input())
h2 = int(input())
h3 = int(input())
d1 = int(input())
d2 = int(input())

x = [h1, h2, h3]

def bubble_swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubbleSort(x):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] > x[i+1]:
                bubble_swap(x, i , i+1)

bubbleSort(x)
sum_h = x[0]

if d1 < d2 :
    sum_d = d1
else:
    sum_d = d2

print(sum_h + sum_d - 50)
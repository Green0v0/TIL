import sys
N = int(sys.stdin.readline().rstrip())
li = []
for i in range(N):
    product_name = sys.stdin.readline().strip()
    li.append(product_name)
price_N = int(sys.stdin.readline().rstrip())
price_li = []
for i in range(price_N):
    product_price = float(sys.stdin.readline().rstrip())
    price_li.append(product_price)
sold_N = int(sys.stdin.readline().rstrip())
sold_li = []
for i in range(sold_N):
    product_sold = sys.stdin.readline().rstrip()
    sold_li.append(product_sold)
sold_price_N = int(sys.stdin.readline().rstrip())
sold_price_li = []
for i in range(sold_price_N):
    sold_price = float(sys.stdin.readline().rstrip())
    sold_price_li.append(sold_price)
sum = 0
for i in range(len(sold_li)):
    for j in range(len(li)):
        if li[j]==sold_li[i]:
            if sold_price_li[i] - price_li[j] == 0:
                continue
            else :
                sum = sum+1
print(sum)
# print(price_li)

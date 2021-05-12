a = input()
a = int(a)
# typeerror
# a = map(int,input())
if a % 400 == 0:
    print(1)
elif a % 100 == 0 and a % 400 != 0 :
    print(0)
elif a % 4 == 0 and a % 100 != 0:
    print(1)
# elif a % 4 == 0:
#     print(1)
else :
    print(0)

# another
if(a % 4 ==0 and a % 100 != 0) or a % 400 == 0:
    print(1)
else :
    print(0)
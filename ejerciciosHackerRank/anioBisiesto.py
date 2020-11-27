def is_leap(year):
    
    if year % 4 == 0:  
        if year % 100 != 0:
            print('True')
    elif year % 400 == 0:
            print('True')
    else: 
        print('False')
    
is_leap(2019)

def suma(n):
    # i = 1
    # while i <= n:
    #     print(i)
    # ++i
    for i in range(n):
        print(i+1, end='')
    
suma(5)

a = {1,2,3,4,5,6,7,8,9}
b = {10,1,2,3,11,21,55,6,8}
# for x in range(1,4):
x = len(a-b)
print(x)
set_1 = set(map(int,input().split()))
o, e = [set(a,b) for i in range(4)][1::2]
print(len(o.difference(e)))

_, a = (input(), set(input().split()))
_, b = (input(), set(input().split()))

print(len(a.difference(b)))
print(len(a.symmetric_difference(b)))
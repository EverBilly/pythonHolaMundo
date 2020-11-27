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

_, a = (input(), set(input.split()))
_, b = (input(), set(input.split()))

print(len(a.difference(b)))
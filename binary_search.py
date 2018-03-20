c = [3, 6, 50, 70, 71, 100, 103, 201, 361]

a = c
x = int(input())
while len(a) != 1:
    f = (len(a)//2)
    if x == a[f]:
        print('Belongs')
        break
    elif x > a[f]:
        del a[:f]
        print(a)
    else:
        del a[f:]
        print(a)

if x != a[0]:
    print('Do not belong')
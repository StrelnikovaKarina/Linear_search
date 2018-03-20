a = [3, 6, 10, 102, 61, 90, 85, 1000]

x = int(input())

for i in range(len(a)):
    if x == a[i]:
        print('Belongs')
        break
if x != a[i]:
    print('Do not belong')
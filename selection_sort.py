a = [90, 10, 20, 60, 5, 1, 6, 500, 2, 3, 0 ]

for i in range(len(a)):
    x = min(a[i:])
    a.remove(x)
    a.insert(i,x)
    print(a)
    i = i + 1
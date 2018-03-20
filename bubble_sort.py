b = [8, 5, 50, 16, 11, 60, 61, 100, 0, 19, 63, 99, 1, 88]
c = 0
while c < len(b):
    for i in range(len(b)):
        if i+1 >= len(b):
            i = 0
        if b[i] > b[i+1]:
            a = b[i+1]
            b[i+1] = b[i]
            b[i] = a
            print(b)
    c = c+1
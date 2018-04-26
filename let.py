height=0

while height <= 1 or height > 24:
    try:
        height = int(input("Height:"))
    except:
        print('Enter the height (height is the number and 0 < height < 24)')


b = 2     # b - number of blocks '#'
while height > 0:
    print(' '*(height-1)+'#'*(b))
    b  += 1
    height -= 1
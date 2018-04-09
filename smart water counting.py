print ('Enter minutes spent in the shower.')

minutes = int(input())

while minutes <= 0:
    print ('Enter minutes (above zero) spent in the shower')
    minutes = int(input())

bottles = minutes * 12

print (bottles, 'bottles')

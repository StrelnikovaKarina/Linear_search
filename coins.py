change = 0      # How much should you give change
fifty = 0      # Number of coins of 50 each
ten = 0      # Number of coins of 10 each
five = 0      # Number of coins of 5 each
one = 0      # Number of coins of 1 each


while change <= 0:      # Check the entered value
    try:
        change = int(input("Your change:"))
    except:
        print('Enter the number of coins')


print("  ***  ")


while change // 50 >=1:      # Calculation of the number of coins of 50 each
    change -= 50
    fifty += 1
if fifty > 0:
    print(fifty, "coins of 50 each")


while change // 10 >=1:      # Calculation of the number of coins of 10 each
    change -= 10
    ten += 1
if ten > 0:
    print(ten, "coins of 10 each")


while change // 5 >=1:      # Calculation of the number of coins of 5 each
    change -= 5
    five += 1
if five > 0:
    print(five, "coins of 5 each")


while change // 1 >=1:      # Calculation of the number of coins of 1 each
    change -= 1
    one += 1
if one > 0:
    print(one, "coins of 1 each")


print("  ***  ")


print("Total:", fifty+ten+five+one, "coins")

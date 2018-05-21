a = (
    ' ', '.', ',', 'a', 'b', 'c', 'd', 'e',
    'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
)

step = int(input("Step: "))
while step > 25 :
    try:
        step = int(input("Step (<26): "))
    except:
        step = int(input("Step (number less than 26): "))

print('Your text can contain English lowercase letters, spaces, dots and commas.')
t = list(input('Text: '))           # t - text for encryption

print('Cipher: ', end="")
for j in range(len(t)):
    i = a.index(t[j])           # i - index of letters in the alphabet
    c = int(i + step)           # e - encrypted letter
    if c > len(a):
        c = ((step+3) - (len(a)-i))
        print(a[c], end="")
    elif i == 0:
        print(' ', end="")
    elif i == 1:
        print('.', end="")
    elif i == 2:
        print(',', end="")
    else:
        print(a[c], end="")
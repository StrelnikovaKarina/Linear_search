a = (
    'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x',
    'y', 'z'
)

spa = []    # indices text's space in the alphabet
index_t = []    # indices text's letters in the alphabet
index_k = []    # indices key letters in the alphabet
index_c = []    # indices cipher's letters in the alphabet
cipher = []

key = list(input("Key: "))
print('Your text can contain English lowercase letters and spaces.')
text = list(input('Text: '))

for k in range(len(key)):
    i_k = a.index(key[k])
    index_k.append(i_k)

for t in range(len(text)):      # adds spaces index to 'spa' and letters index to 'index_t'
    if text[t] == ' ':
        spa.append(t)
    else:
        i_t= a.index(text[t])
        index_t.append(i_t)

i = len(index_t)//len(index_k)

# calculates letters index for the cipher
while i != 0:
    for k in range(len(index_k)):
        c = (index_t[0]) + (index_k[k])
        index_c.append(c)
        del index_t[0]
    i -=1

for t in range(len(index_t)):
    k=t
    s = (index_t[t]) + (index_k[k])
    index_c.append(s)
del index_t

# translate the index into a letter
for c in range(len(index_c)):
    if index_c[c] >= len(a):
        v = index_c[c] - len(a)
        cipher.append(a[v])
    else:
        cipher.append(a[index_c[c]])

# adds spaces to the cipher
for j in range(len(spa)):
    cipher.insert(spa[j],' ')


for g in range(len(cipher)):
    print(cipher[g], end="")
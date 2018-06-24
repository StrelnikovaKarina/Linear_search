founders = {'Guido van Rossum': 'Python',
     'James Gosling': 'Java',
     'Larry Wall': 'Perl',
     'Roberto Ierusalimschy': 'Lua',
     'Rasmus Lerdorf': 'PHP',
     'Rodrigo Barreto de Oliveira':'Boo',
     'Rob Pike':'Go',
     'Dennis Ritchie':'C'
}

def dictionary():
    for key in founders:
        print('*', key, ' - ', founders[key])

# Dictionary keys sort function A-Z
def sort():
    for key in sorted(founders.keys()):
        print('*', key, ' - ', founders[key])

# Dictionary keys sort function Z-A
def re_sort():
    for key in reversed(sorted(founders.keys())):
        print('*', key, ' - ', founders[key])

# Search function key in dictionary
def search():
    list = []
    for k in founders:
        list.append(k)
    for i in range(len(list)):
        if x in list[i]:
            print(list[i], '-', founders[list[i]])

print('Enter the')
print('           dict (if you want to see the dictionary)')
print('           az (if you need a sorted dictionary A-Z)')
print('           za (if you need a sorted dictionary Z-A)')
print('           search (if you need a search by name)')
print('           end (if you are finished)')

a = input('You need: ')

while a != 'end':
    if a == 'dict':
        dictionary()
    if a == 'az':
        sort()
    if a == 'za':
        re_sort()
    if a == 'search':
        x = input('Name: ')
        search()
    print('========')
    a = input('You need: ')
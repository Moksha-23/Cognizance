rows = int(input('Enter the rows :'))
spaces = rows
number = 1
for i in range(1, rows + 1, 1):
    for j in range(1, spaces + 1, 1):
        print(' ', end='', flush=True)
    spaces = spaces - 1
    for q in range(1, i + 1, 1):
        print('*', end='', flush=True)
        number = number + 1
        print(' ', end='', flush=True)
    print('')

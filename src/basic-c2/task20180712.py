print(' 1|  2  3  4  5  6  7  8  9')
print('--+-----------------------')
print('| \n' *10)
for x in range(0,9):
    for y in range(0,9):
            print('{0}'.format('%2d ' % ((x+1) * (y+1))), end="")
    print('')

import numpy as np
x = np.arange(7, 16)
y = np.arange(1, 18, 2)
z = np.column_stack((x[::-1], y))
for i, j in z:
    print(' ' * i + '*' * j)
for r in range(3):
    print(' ' * 13, ' || ')
print(' ' * 11, end = ' \ ____ / ')
print('\n')

# numpy nélkül
for i in range(1,10):
    print((10-i)*' ', (i*2-1)*'*')
for r in range(3):
    print(' ' * 8, '||')
print(' ' * 5, end = ' \ ____ / ')

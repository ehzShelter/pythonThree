def mario(n=2):
    for row in range(n):
        for col in range(n):
            if row + col < n - 1:
                print(' ', end='')
            else:
                print('#', end='')
        print('#')


# mario(10)

# If you want to call like C
if __name__ == '__main__':
    mario(10)

# python magic
print('\n')
print('%' * 5)
print('#' * 7)
print('marioMagic Implementaton')


def marioMagic(n=10):
    # remember row indexing start from zero
    for row in range(n):
        print((' ' * (n - row - 1)) + (('#' * row) + '##'))

marioMagic(15)

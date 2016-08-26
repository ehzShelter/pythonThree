n = 10

def mario():
    for row in range(n):
        for col in range(n):
            if row + col < n - 1:
                print(' ', end='')
            else:
                print('#', end='')
        print('#')


mario()

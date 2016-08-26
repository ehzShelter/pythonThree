def mySearch():
    needle = 42

    hayStack = [41 + i for i in range(5)]

    if needle in hayStack:
        return True
    return False

# this will give you address
print(mySearch)
# this is actual function call, and will give you value
print(mySearch())

ary = [1, 7, 5, 4, 0, 6, 3, 2]
print(ary)

print(sorted(ary))
print(sorted(ary, reverse=True))

strAry = ['cat', 'cs50!', 'ban']
print(sorted(strAry))


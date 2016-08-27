import numpy


x = numpy.ones(3)

m = numpy.eye(3)

print(x)
print(m)

print(x @ m)

# this is actually list
y = [[1, 2, 3],
     [2, 3, 4],
     [5, 6, 9]]

print(y)

l = [[2, 2, 2]]

print(l)

# TypeError: unsupported operand type(s) for @: 'list' and 'list'
# print( y @ l)

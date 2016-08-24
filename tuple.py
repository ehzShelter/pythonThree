t = 12345, 54321, 'hello!'

print(t[0])
print(t)

# tuple may be nested
u = t, (1, 2, 3, 4)

print (u)
print (t[0])

# you can not mutate tuple value
# t[0] = 8855
# TypeError: 'tuple' object does not support item assignment
# tuples are immutable

# But they can contain mutable objects
v = ([1, 2, 3], [3, 8, 9])
print(v)

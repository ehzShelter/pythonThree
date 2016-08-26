class Dog:
    sharedVarByClass = 'I am shared across all class instances'

    def __init__(self, name):
        self.name = name

d = Dog('Fido')
e = Dog('Dido')

print(d.sharedVarByClass)
print(e.sharedVarByClass)

print(d.name)
print(e.name)

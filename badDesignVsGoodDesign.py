class Dog:
    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
print(d.tricks)                # unexpectedly shared by all dogs
e.add_trick('play dead')
# buggy results
print(d.tricks)                # unexpectedly shared by all dogs

print('\n')

class Pitbull:
    def __init__(self, name):
        self.name = name
        # better to decleare container as instance variable
        self.tricks = []

    def addTrick(self, trick):
        self.tricks.append(trick)


d = Pitbull('Fido')
e = Pitbull('Buddy')
d.addTrick('roll over')
print(d.tricks)
e.addTrick('play dead')
#expected result
print(d.tricks)

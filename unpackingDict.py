myString = "Hi , my name is {name} and I live in {state}"

demo = myString.format(name = 'Sohan', state = 'Ctg')
print(demo)
myDict = {'name': 'Zawad', 'state' : 'Dhaka'}

hell = myString.format(**myDict)
print (hell)
# remember string is immutable
print (myString)

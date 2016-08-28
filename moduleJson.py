import json

f = open('sample.json', 'r')

thing = json.load(f)

# flush and close filIO object
# this method has no effect, If the file is already closed
f.close()

print(sample)

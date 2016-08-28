dict = {}

# key => maps to various values
dict['Rob'] = 'Bowden'
dict['Tommy'] = 'Macwilliam'
dict['Emrul'] = ['Hasan', 'Zawad']

print(dict['Rob'])
print(dict['Emrul'])

# keyError
# print(dict['Abrar'])

#
# def load(dictFile):
#     dict = {}
#
# # open file in python in readonly mode
#     df = open(dictFile, 'r')
#
#     for line in df:
#         word = line[:-1]
#         dict[word] = 1 # dummy value
#
#     # return from load() function
#     return dict
#


# def check(word, dict):
#     if word in dict:
#         # in python True not true
#         # cations
#         # in python False not false
#         return True
#     return False

# +   addition
# -   subtraction
# *   multiplication
# /   division
# **  exponent (power)
# %   modulo (remainder after division)
# //  floor division (rounds down to nearest whole number)



# Empty lists
empty_list = []
empty_list = list()

# # Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# # Empty Sets
empty_set = {} # This isn't right! It's a dictionary
empty_set = set() # This is the correct way to create an empty set.


# --- Dictionarys ---

empty_dict = {} # As previously mentioned above.

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

= {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}


student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['age'])

= Prints out the varible 'age' === 25.


# --- Conditionals + Booleans ---

langauge = 'Python'


if langauge == 'Python':
    print('Conditional was true.')

= Prints out 'Conditional was true'.

# Comparisions:
# Equal:              ==
# Not Equal:          !=
# Greater Than:       >
# Less Than:          <
# Greater or Equal:   >=  
# Less or Equal:      <=
# Object Identity:    is

# and
# or
# not

langauge = 'C++'

if langauge == 'Python':
    print('Langauge is Python')
else:
    print('No match')

= 'No match' will be printed because the langauge varible is set to C++.


langauge = 'JavaScript'


if langauge == 'Python':
    print('Langauge is Python')
elif langauge == 'C++':
    print('Langauge is C++')
elif langauge == 'JavaScript':
    print('Langauge is JavaScript')
else:
    print('No match')

= 'Langauge is JavaScript' will be printed. 


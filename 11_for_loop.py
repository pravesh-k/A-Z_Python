# For Loop: It is used for sequential traversal i.e. it is used for iterating 
#           over an iterable like string, tuple, list, dictionary, etc. It 
#           falls under the category of definite iteration. 
# 
#           Definite iterations mean the number of repetitions is specified 
#           explicitly in advance. 
#           
#           In Python, there is no C style for loop, 
#           i.e., for (i=0; i<n; i++). 
#           There is “for in” loop which is similar to 
#           for each loop in other languages

'''
syntax:
for var in iterable:
    statement(S)
'''


# # Content:
#   1. for-loop on different iterable data structures
#   2. Single statement for loops
#   3. Loop Control Statements
#   4. range function
#   5. While loop with else


# 1. for-loop on different iterable data structures

# a. while loop with strings
# Example 1:
note = 'Hello Developers'
for letter in note:
    print(letter, end=" + ")
print('\n')     # this line is out of for loop block

# b. while loop with lists
# Example 1:
lst = ['a', 2, 'Hi', True, 3, 6, 9, 12]
for item in lst:
    print(item, end=" * ")
print('\n')

# Example 2: while loop on list of lists
lst = [['a', 2, 'Hi'], [2, 3, 5, 7, 11]]
for i in lst:
    for j in i:
        print(j, end=" - ")
    print()
print()

# c. while loop with tuples
# Example 1:
direction_tuple = ('North', 'South', 'East', 'West', 'Center')
for item in direction_tuple:
    print(item, end=" > ")
print('\n')

'''for tuple of tuples, for loop can be implemented as in list of lists'''

# d. while loop with sets
decision_set = {'yes', 'no', 'maybe', 'non-decisive'}
for each in decision_set:
    print(each, end=' / ')
print('\n')
'''note that the order of items in set changes each time as sets are UNORDERED objects'''

# e. while loop with dictionaries

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": ['Red', 'Blue', 'White'],
    "EV": False
    }
# Example 1: iterating through a dict returns only keynames on each iteration
for each in car_dict:
    print(each)
print()

# Example 2: iterating through dict.items() returns key-value in tuple objects
for each in car_dict.items():
    print(each)
print()

# Example 3: alternative way to loop through dict.items() to avoid returning of 
# key-values inside tuple container
for x, y in car_dict.items():
    print(x, y)
print()


# Example 4: iterating through dict.keys() is same as iterating through a 
# dictionary object and returns keynames
for each in car_dict.keys():
    print(each)
print()

# Example 5: iterating through dict.values() returns values
for each in car_dict.values():
    print(each)
print()

# Example 6: alternative way to get the values of the dictionary without using 
# values() method
for each in car_dict:
    print(car_dict[each])
print()


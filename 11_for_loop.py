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
#   2. range function
#   3. Single statement for loops
#   4. Loop Control Statements
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


# 2. range function:
'''
**note 1: range() is a built-in function that is used when a user needs to perform 
an action a specific number of times. The range() function is used to generate a 
sequence of numbers. Depending on how many arguments user is passing to the 
function, user can decide where that series of numbers will begin and end as well 
as how big the difference will be between one number and the next. range() 
function takes mainly three arguments. 

    start: integer starting from which the sequence of integers is to be returned
    stop: integer before which the sequence of integers is to be returned. 
    The range of integers end at stop - 1.
    step: integer value which determines the increment between each integer in the
    sequence 
    
    syntax:
    variable = range(start, stop, step)
    '''

# Example 1: for loop with range() but with only 1 argument passed to range().
for i in range(5):
    print(i, end=", ")
print('\n')

# Example 2: for loop with range() with 2 arguments passed to range()
for j in range(2, 8):
    print(j, end=", ")
print('\n')

# Example 3: for loop with range() with 3 arguments passed to range()
for k in range(0, 15, 3):
    print(k, end=", ")
print('\n')

# Example 4: using range() to iterate through lists via indexes
lst2 = [2, 8, 15, 74, 100]
for i in range(len(lst2)):
    print(lst2[i], end='" ')
print('\n')

# Example 5: using range() to iterate through tuple via indexes
tpl2 = ('A', 'E', 'I', 'O', 'U')
for i in range(len(tpl2)):
    print(tpl2[i], end='! ')
print('\n')

'''note that set and dictionary objects can not be accesses via indexes'''

# 3. Single statement for-loops

# Example 1: single-line for loop
for i in range(4): print(i, end='$ '); print('=Rs. ', 74*i)
print()

# Example 2: list comprehension for list creation
cubes = [x**3 for x in range(10) if x % 2 == 0]
print(f'cubes : {cubes}\n')


# 4. Loop Control Statements

# a. continue statement: continue statement returns the control to the beginning 
# of the loop.
# Example 1
for i in range(5):
    print('Indian')
    continue
    print('Non-Indian')     # this line is never executed due to conitnue statement
print()

# Example 2: print all letters except 'l' and 'o'
welcome = 'HelloFolks,WelcomeToTheWhileLoop'
for letter in welcome:
	if letter == 'l' or letter == 'o':
		continue
	print(letter, end=" ")
print()

# b. break statement: break statement brings control out of the loop.
# Example 1:
for i in range(3):
    print('\nAmerican', i)
    break
    print('Non-American', i)     # this line is never executed due to break statement
print()

# Example 2: break the loop as soon as 'o' is found
welcome = 'HelloFolks,WelcomeToTheWhileLoop'
for letter in welcome:
	if letter == 'o':
		break
		
	print(letter, end=" ")
print('\n')


# 5. for loop with else
# The else block just after for is executed only when the loop is NOT terminated 
# by a break statement

'''
syntax:
for var in iterable:
    statement(s)
else:
    statement(s)
'''

# Example 1: simple for-else loop
for i in range(1, 4):
	print(i)
else:                   # Executed because no break in for
	print("No Break\n")

# Example 2: for-else loop along with break statement
for i in range(1, 4):
	print(i)
	break
else:                   # Not executed as there is a break
	print("No Break")
# While Loop: It is used to execute a block of statements repeatedly until a
#             given condition is satisfied. And when the condition becomes false, 
#             the line immediately after the loop in the program is executed. 
#             While loop falls under the category of indefinite iteration. 

#             Indefinite iteration means that the number of times the loop is   
#             executed isn’t specified explicitly in advance. 

'''
syntax:
while expression:
    statement(S)
'''


# # Content:
#   1. While loop
#   2. Single statement while block
#   3. Loop Control Statements
#   4. While loop with else
#   5. While loop on different data structures


# 1. While loop

# Example 1: printing Hello World three times
count = 0
while count < 3:        # iterate this block till value of count is less than 3
    count = count + 1       # increment the value of count by 1
    print(f'Hello World {count}')
print()     #this line is out of while block


# 2. Single statement while block

# Example 1: multi-statement inside single statement while loop
count = 3
while count < 6: count = count + 1; print(f'Hello Python {count}')
print()

# Example 2: nested compound statements inside single statement while loop
steps = 0
while steps < 6: print(f'Bonjour! {steps}') if steps % 2 == 0 else print(f'Adios {steps}'); steps += 1
'''note that short-hand if-else statement is used'''
print()


# 3. Loop Control Statements

# a. continue statement: continue statement returns the control to the beginning 
# of the loop.
# Example 1
count = 0
while count < 3:
    count += 1
    print('Indian')
    continue
    print('Non-Indian')     # this line is never executed due to conitnue statement
print()

# Example 2: print all letters except 'l' and 'o'
welcome = 'HelloFolks,WelcomeToTheWhileLoop'
index = 0

while index < len(welcome):
	if welcome[index] == 'l' or welcome[index] == 'o':
		index += 1
		continue
		
	print(welcome[index], end=" ")
	index += 1
print()

# b. break statement: break statement brings control out of the loop.
# Example 1:
count = 0
while count < 3:
    count += 1
    print('\nAmerican')
    break
    print('Non-American')     # this line is never executed due to break statement
print()

# Example 2: break the loop as soon as 'o' is found
welcome = 'HelloFolks,WelcomeToTheWhileLoop'
index = 0

while index < len(welcome):
	if welcome[index] == 'o':
		index += 1
		break
		
	print(welcome[index], end=" ")
	index += 1
print('\n')


# 4. While loop with else
# While loop is only executed when the condition is true but when the condition is 
# false, else clause is executed. If there is a break statement in the loop, or if 
# an exception is raised, else block is not executed.

'''
syntax:
while expression:
    statement(s)
else:
    statement(s)
'''

# Example 1: simple while-else loop
i = 0
while i < 2:
    print(f'i = {i}')
    i += 1
else:       # after the condition in while loop is false, this block is executed
    print('Otherwise\n')

# Example 2: while-else loop with break statement
j = 1
while j < 30:
    print(f'j = {j}')
    j += 1
    break
else:       # this else block will never be executed due to the break in while
    print('Otherwise\n')
print()


# 5. While loop on different data structures

# a. while loop with strings
'''an example can be found in section 3.a.Example 2'''
# Example 1:
note = 'Hello Developers'
i = 0
len_of_note = len(note)
while i < len_of_note:
    print(note[i], end=", ")
    i += 2

print('\n')

# b. while loop with lists
# Example 1:
lst = ['a', 2, 'Hi', True, 3, 6, 9, 12]
i = 0
len_of_lst = len(lst)
while i < len_of_lst:
    print(lst[i], end=" > ")
    i += 1

print('\n')

# Example 2: while loop on list of lists
lst = [['a', 2, 'Hi'], [2, 3, 5, 7, 11]]
i = 0
len_of_lst = len(lst)
while i < len_of_lst:
    j = 0
    item = lst[i]
    len_of_item = len(lst[i])

    while j < len_of_item:
        print(item[j], end=" > ")
        j += 1
    print()
    i += 1

print()

# c. while loop with tuples
# Example 1:
direction_tuple = ('North', 'South', 'East', 'West', 'Center')
i = 0
len_of_direction_tuple = len(direction_tuple)
while i < len_of_direction_tuple:
    print(direction_tuple[i], end=" > ")
    i += 1

print('\n')

'''for tuple of tuples, while loop can be implemented as in list of lists'''

# d. while loop with sets
'''**note 1:
Since set objects are UNORDERED we can access it via indexes thus implementing while loop for set object is not possible but other looping methods like for-loop can be implemented with sets
'''

# e. while loop with dictionaries
# Example 1:
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": ['Red', 'Blue', 'White'],
    "EV": False
    }

# len_of_car_dict = len(car_dict)
# i = 0
# while i < len_of_car_dict:
#     print(car_dict[i], end=" | ")
#     i += 1
'''
**note 2:
the above piece of code won't work as dict accepts keynames inside square 
brackets and not indexes
Thus we can only iterate through the list view of keys or values of the 
dictionary, i.e. first we have to typecast the view of dict.keys() and 
dict.values() and dict.items() to list type objects, then only we can implement 
while loop. This means there is no way to implement while loop directly on 
dictionary objects.
'''
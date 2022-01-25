# Lists in Python: Lists are used to store multiple items in a single variable.
            # It is one of 4 built-in data types in Python used to store
            # collections of data. Lists is a mutable data container.
            # List items are mutable (change, add, and remove), and allow duplicate values.
            # List items are indexed, the first item has index [0],
            # the second item has index [1] etc.

# # Contents:
#   1. Defining Lists
#   2. printing lists
#   3. Accessing items from list
#   4. Copying a list to another variable
#   5. List methods provided by Python3
#   6. List Comprehensions


# 1. Defining a list

# creating an empty list


empty_list_1 = []
empty_list_2 = list()

# list with all items having type int
prime_num_list = [5, 2, 3, 11, 7, 17, 13]
magic_num_list = list((2, 8, 20, 28, 50))       #note the double parentheses

# list with all items having type string
fruit_list = ["apple", "banana", "cherry"]

# list with all items having type boolean
bool_list = [True, False, True, True, False]

# list with items having different types
emp_det_list = ['John Walker', 30, 'Manager', 'Sales', 2.55, 98000, True]

# list having another lists as items
list_of_lists = [['banana', 'guava'], [True, False, True], [0, 15, 17, 55]]


# 2. printing lists

print('empty_list_1:\n', empty_list_1,
    '\nempty_list_2:\n', empty_list_2,
    '\nprime_num_list:\n', prime_num_list,
    '\nmagic_num_list:\n', magic_num_list,
    '\nfruit_list:\n', fruit_list,
    '\nbool_list:\n', bool_list,
    '\nemp_det_list:\n', emp_det_list,
    '\nlist_of_lists:\n', list_of_lists,
    '\n'
    )


# 3. Accessing items from list

# access single item
print('fruit_list[0] =', fruit_list[0],
    '\nprime_num_list[2] =', prime_num_list[2],
    '\nlist_of_lists[0] =', list_of_lists[0],
    '\nlist_of_lists[0][1] =', list_of_lists[0][1],
    '\n'
    )

# access a sub sequence from the list/ this is 
# also referred to as slicing a list
print('fruit_list[0:1] =', fruit_list[0:2],
    '\nprime_num_list[1:3] =', prime_num_list[1:3],
    '\nlist_of_lists[1:2] =', list_of_lists[1:2],
    '\n'
    )

# access sub sequence from a list but with 
# a step/hop between items
# template of slice operator: a_list[start:end:step]
print('prime_num_list[0:4:2] =', prime_num_list[0:4:2],
    '\nprime_num_list[0:6:2] =', prime_num_list[0:6:3],
    '\n')

# access sub sequence from a list but from end to start
print('prime_num_list[4:0:-1] =', prime_num_list[4:0:-1],
    '\nprime_num_list[6:0:-1] =', prime_num_list[6:0:-1],
    '\nprime_num_list[6:0:-2] =', prime_num_list[6:0:-2],
    '\n')

# to access all items of list using slicing
print('prime_num_list[:] =', prime_num_list[:],
    '\nprime_num_list[::-1] =', prime_num_list[::-1],
    '\n')

# some more examples of slicing
print('prime_num_list[:3] =', prime_num_list[:3],
    '\nprime_num_list[3:] =', prime_num_list[3:],
    '\nprime_num_list[-3:] =', prime_num_list[-3:],
    '\nprime_num_list[:-3] =', prime_num_list[:-3],
    '\nprime_num_list[::2] =', prime_num_list[::2],
    '\n'
    )


'''
***************************************************
**note 1: inbuilt function id() can be used to find 
      the memory address of any variable in python3

example:
print('memory address of fruit_list =', id(fruit_list),
    '\n'
    )
***************************************************
'''


# 4. Copying a list to another variable

# copying a list to another variable will 
# create an exact copy with same memory location
copy_prime_num_list = prime_num_list
print('prime_num_list =', prime_num_list,
    '\ncopy_prime_num_list =', copy_prime_num_list,
    '\nmemory address of prime_num_list =', id(prime_num_list),
    '\nmemory address of copy_prime_num_list =', id(copy_prime_num_list),
    '\n'
    )

# shallow copying the list to a variable will
# will be stored in a different memory location
copy2_prime_num_list = prime_num_list[:]
print('prime_num_list =', prime_num_list,
    '\ncopy2_prime_num_list =', copy2_prime_num_list,
    '\nmemory address of prime_num_list =', id(prime_num_list),
    '\nmemory address of copy2_prime_num_list =', id(copy2_prime_num_list),
    '\n'
    )


'''
***************************************************
**note 2: inbuilt function len() can be used to return 
      the length (the number of items) of an object. 
      The argument may be a sequence (such as a string, 
      bytes, tuple, list, or range) or a collection 
      (such as a dictionary, set, or frozen set).

example:
print('length of list fruit_list =', len(fruit_list),
    '\n')
***************************************************
'''


# 5. List methods provided by Python3

# a. Add and item to the end of the list
#    syntax: a_list.append(object)
prime_num_list.append(19)
print('prime_num_list =', prime_num_list,
    '\n'
    )
# the append function is equivalent to the below operation
prime_num_list[len(prime_num_list):] = [23]     # notice the square brackets around 23
print('prime_num_list =', prime_num_list,
    '\n'
    )


'''
***************************************************
**note 3: Iterable is an object which can be looped over 
      or iterated over with the help of a for loop. Objects 
      like lists, tuples, sets, dictionaries, strings, etc. 
      are called iterables.
***************************************************
'''


# b. Extend the list by appending all the items from the iterable
#    syntax: a_list.extend(iterable_object)
more_fruits_list = ['grapes', 'pineapple']
fruit_list.extend(more_fruits_list)
print('fruit_list =', fruit_list,
    '\n'
    )

# the append function is equivalent to the below operation
extra_fruit_lists = ['mango', 'strawberry']
fruit_list[len(fruit_list):] = extra_fruit_lists
print('fruit_list =', fruit_list,
    '\n'
    )
# c. Insert an item at a given position
#    syntax: a_list.insert(index, object)
more_fruits_list.insert(1, 'blackberry')
print('more_fruits_list =', more_fruits_list,
    '\n'
    )

# imitating functionality of append method using insert method
more_fruits_list.insert(len(more_fruits_list), 'orange')
print('more_fruits_list =', more_fruits_list,
    '\n'
    )

# d. Remove the item at the given position in the list, and return it
#    If no index is specified, removes and returns the item at the last
#    syntax: a_list.pop(index_optional)
print('more_fruits_list.pop(2) =', more_fruits_list.pop(2),
    '\nmore_fruits_list =', more_fruits_list,
    '\n'
    )

print('prime_num_list.pop() =', prime_num_list.pop(),
    '\n')


'''
***************************************************
**note 4: 'del' keyword  in python is primarily used 
      to delete objects in Python. Since everything in 
      python represents an object in one way or another, 
      The del keyword can also be used to delete a list, 
      slice a list, delete a dictionaries, remove key-value 
      pairs from a dictionary, delete variables, etc.

example:
x = 15
print('x =', x)
del x
print('x =', x)       # This raises a name error
***************************************************
'''


# e. Remove all items from the list.
#    syntax: a_list.clear()
prime_num_list.clear()
print('after clear() methods, prime_num_list =', prime_num_list,
    '\n')

# this is equivalent to the below operation
del copy_prime_num_list[:]
print('using the alternate way, copy_prime_num_list =', copy_prime_num_list,
    '\n')


# f. Return zero-based index in the list of the first 
#    item whose value is equal to x. Raises a ValueError 
#    if there is no such item.
#    syntax: a_list.index(element, start, end) 
#            where start and end parameters are optional
print('fruit_list.index("cherry")', fruit_list.index('cherry'),
    '\nfruit_list.index("pineapple", 3)', fruit_list.index('pineapple', 3),
    '\nfruit_list.index("grapes", 1, 4)', fruit_list.index('grapes', 1, 4),
    '\n')

# g. Return the number of times an element/item appears in the list
#    syntax: a_list.count(element)
print('bool_list.count(True)', bool_list.count(True),
    '\nbool_list.count(False)', bool_list.count(False),
    '\nbool_list.count("Hello")', bool_list.count('Hello'),
    '\nmore_fruits_list.count("blackberry")', more_fruits_list.count('blackberry'),
    '\n'
    )

# h. Sort the items of the list in place.
#    The same functionality is obtained using python inbuilt function
#    name 'sorted()'. This function is helpful to sort other sequence
#    data type as well.
#    syntax: a_list.sort(key, reverse)
#            where key and reverse parameters are optional
print('copy2_prime_num_list =', copy2_prime_num_list)

copy2_prime_num_list.sort()
print('In ascending order, copy2_prime_num_list.sort() \n =', copy2_prime_num_list)

copy2_prime_num_list.sort(reverse=True)
print('In descending order,copy2_prime_num_list.sort(reverse=True) \n =', copy2_prime_num_list, '\n')

print('more_fruits_list\n =', more_fruits_list)

more_fruits_list.sort(key=len)      #len function is used as key
print('In ascending order,using defined order to sort, i.e. sort by\n the element length, more_fruits_list.sort(key=len) \n =', more_fruits_list, '\n')

# i. Reverse the elements of the list in place.
#    syntax: a_list.reverse()
print('copy2_prime_num_list =', copy2_prime_num_list)
copy2_prime_num_list.reverse()
print('reversing the list elements by position\n copy2_prime_num_list.reverse() =', copy2_prime_num_list)

# The above method can be replicated by the below operation
print('copy2_prime_num_list[::-1] =', copy2_prime_num_list[::-1], '\n')

# j. Return a shallow copy of the list
#    syntax: list.copy()
copy_more_fruits_list = more_fruits_list.copy()
print('copy_more_fruits_list =', copy_more_fruits_list)

# This can be achieved using the below operation
copy2_more_fruits_list = more_fruits_list[:]
print('copy2_more_fruits_list =', copy2_more_fruits_list, '\n')


# 6. List Comprehensions

# A normal approach to form a list of squares of few whole numbers
squares_1 = []
for x in range(6):
    squares_1.append(x**2)
print('squares_1 =', squares_1)

# the above operation can be reduced to a concise and 
# readable piece of code in a single line using list comprehension
squares_2 = [x**2 for x in range(6)]
print('squares_2 =', squares_2)

# more examples
# using normal for loop
combs = []
for x in [1,2,3]:
     for y in [3,1,4]:
         if x != y:
             combs.append((x, y))
print('combs =', combs)

# using list comprehension
print([(x,y) for x in [1,2,3] for y in [3,1,4] if x != y])

# note the order of for and if statements in both the implementation
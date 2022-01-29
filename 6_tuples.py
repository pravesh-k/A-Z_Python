# Tuples in Python: A Tuple is a collection of Python objects separated by commas. 
                # In someways a tuple is similar to a list in terms of indexing, 
                # nested objects and repetition but a tuple is immutable unlike
                # lists which are mutable.


# # Contents:
#   1. Creating tuples
#   2. Printing tuples
#   3. Accessing tuples elements
#   4. Immutable behaviour check
#   5. Operations on/with tuples
#   6. Tuple built-in methods


# 1. Creating tuples

# empty tuple
empty_tuple_1 = ()
empty_tuple_2 = tuple()

# tuple with one element
# one_ele_tuple = (1)   # This will create an int type variable
one_ele_tuple_1 = (1,)    # This definition with comma creates a tuple
one_ele_tuple_2 = tuple((1,))

# tuple with repeated elements
rep_ele_tuple = ('Hello', )*3      #note the comma after Hello

# tuple with all items having type int
direction_tuple = 'east', 'west', 'north', 'south'      #note no parentheses
prime_num_tuple = (5, 2, 3, 11, 7, 17, 13)
magic_num_tuple = tuple((2, 8, 20, 28, 50))       #note the double parentheses

# tuple with all items having type string
fruit_tuple = ("apple", "banana", "cherry")

# tuple with all items having type boolean
bool_tuple = (True, False, True, True, False)

# tuple with items having different types
emp_det_tuple = ('John Walker', 30, 'Manager', 'Sales', 2.55, 98000, True)

# tuple having another tuples as items
tuple_of_tuples = (('banana', 'guava'), (True, False, True), [0, 15, 17, 55])
        #note a list as an element of a tuple


# 2. Printing tuples

print(f'empty_tuple_1 : {empty_tuple_1}'
    f'\nempty_tuple_2 : {empty_tuple_2}'
    f'\none_ele_tuple_1 : {one_ele_tuple_1}'
    f'\none_ele_tuple_2 : {one_ele_tuple_2}'
    f'\nrep_ele_tuple : {rep_ele_tuple}'
    f'\ndirection_tuple : {direction_tuple}'
    f'\nprime_num_tuple : {prime_num_tuple}'
    f'\nmagic_num_tuple : {magic_num_tuple}'
    f'\nfruit_tuple : {fruit_tuple}'
    f'\nbool_tuple : {bool_tuple}'
    f'\nemp_det_tuple : {emp_det_tuple}'
    f'\ntuple_of_tuples : {tuple_of_tuples}'
    '\n')

# 3. Accessing tuples elements

# Tuple items can be accessed by referring to the index number, 
# inside square brackets just as we do with lists
# a. Accessing single elements from the tuple
print(f'direction_tuple[0] : {direction_tuple[0]}'
    f'\ndirection_tuple[3] : {direction_tuple[3]}'
    f'\ntuple_of_tuples[2] : {tuple_of_tuples[2]}'
    '\n')

# b. Accessing single elements indexed backwards (starting from the last)
print(f'direction_tuple[-1] : {direction_tuple[-1]}'
    f'\ndirection_tuple[-3] : {direction_tuple[-3]}'
    f'\ntuple_of_tuples[-2] : {tuple_of_tuples[-2]}'
    '\n')

# c. Accessing a sub-sequences in a tuple/slicing through a tuple
print(f'prime_num_tuple[:] : {prime_num_tuple[:]}'
    f'\nprime_num_tuple[2:5] : {prime_num_tuple[2:5]}'
    # f'\nprime_num_tuple[5:2] : {prime_num_tuple[5:2]}'      #invalid index range
    # f'\nprime_num_tuple[-2:-5] : {prime_num_tuple[-2:-5]}'  #invalid index range
    f'\nprime_num_tuple[-5:-2] : {prime_num_tuple[-5:-2]}'
    f'\nprime_num_tuple[2:] : {prime_num_tuple[2:]}'
    f'\nprime_num_tuple[:4] : {prime_num_tuple[:4]}'
    f'\nprime_num_tuple[-2:] : {prime_num_tuple[-2:]}'
    f'\nprime_num_tuple[:-5] : {prime_num_tuple[:-2]}'
    '\n')

# d. Accessing a sub-sequences in a tuple/slicing but with a step
print(f'prime_num_tuple[::2] : {prime_num_tuple[::2]}'
    f'\nprime_num_tuple[::3] : {prime_num_tuple[::3]}'
    f'\nprime_num_tuple[2:5:2] : {prime_num_tuple[2:5:2]}'
    f'\nprime_num_tuple[-5:-2:2] : {prime_num_tuple[-5:-2:2]}'
    '\n')

# e. Accessing all elements starting from last
print(f'prime_num_tuple[::-1] : {prime_num_tuple[::-1]}'
    f'\nprime_num_tuple[::-2] : {prime_num_tuple[::-2]}'
    '\n')


# 4. Immutable behaviour check

# Updating elements of tuple
# prime_num_tuple[2] = 19       # Raises TypeError
# prime_num_tuple.append(19)    # Raises AtrributeError
# prime_num_tuple.remove(5)     # Raises AtrributeError

'''
The above operations (modify, add, remove) on values of tuple 
are not allowed and thus tuples prove to be immutable
'''


# 5. Operations on/with tuples

# a. Concatenation of tuples
odd_num_tuple = 1, 3, 5, 7
even_num_tuple = 2, 4, 6, 8
num_tuple = odd_num_tuple + even_num_tuple
print(f'odd_num_tuple : {odd_num_tuple}'
    f'\neven_num_tuple : {even_num_tuple}'
    f'\nnum_tuple : {num_tuple}'
    '\n')

# b. Deletion of a tuple
del odd_num_tuple
# print(f'odd_num_tuple : {odd_num_tuple}\n')      # Raises NameError

# c. Mutable list as an item in a tuple
'''
If a list is present as an item in a tuple, then the list item will follow the original behaviour of a list but other items of the tuple will follow the behviour of tuple except the list items.
'''

tuple_of_tuples[2][0] = 5
tuple_of_tuples[2].append(100)
tuple_of_tuples[2].pop(2)
print(f'tuple_of_tuples : {tuple_of_tuples}\n')

# d. Type-casting tuple into list and set
even_num_list = list(even_num_tuple)
even_num_set = set(even_num_tuple)
print(f'type of even_num_list : {type(even_num_list)}'
    f'\ntype of even_num_set : {type(even_num_set)}\n'
    '\n')

# e. Finding length, max and min of a tuple
print(f'length of even_num_tuple : {len(even_num_tuple)}'
    f'\nmin of even_num_tuple : {min(even_num_tuple)}'
    f'\nmax of even_num_tuple : {max(even_num_tuple)}'
    '\n')

# f. Type-casting string, list and set into tuple
str1_to_tuple = tuple('Python')
str2_to_tuple = tuple(('Python',))
list_to_tuple = tuple([0, 6, 8, 10, 101])
set_to_tuple = tuple({1, 1, 0, 3, 1, 2, 4})

print(f'str1_to_tuple : {str1_to_tuple}'
    f'\nstr2_to_tuple : {str2_to_tuple}'
    f'\nlist_to_tuple : {list_to_tuple}'
    f'\nset_to_tuple : {set_to_tuple}'
    '\n')

# g. Unpacking tuples
# We can extract the items from tuples and assign them to variables
a, b, c, d = even_num_tuple
print(f'a : {a}, b : {b}, c : {c}, d : {d}\n')

# If items in tuples are more than variable count, then use astericks (*)
# with the variable to assign more than one item from tuple as a list

a, b, c, *d = num_tuple
print(f'a : {a}, b : {b}, c : {c}, d : {d}\n')
a, b, *c, d = num_tuple
print(f'a : {a}, b : {b}, c : {c}, d : {d}\n')
*a, b, c, d = num_tuple
print(f'a : {a}, b : {b}, c : {c}, d : {d}\n')


# 6. Tuple built-in methods

# a. Return the number of times a specified item occurs in a tuple
#    syntax: a_tuple.count(value)
print(f'count of True in bool_tuple : {bool_tuple.count(True)}'
    f'\ncount of False in bool_tuple : {bool_tuple.count(False)}'
    '\n')

# b. Search for the first occurrence of the value, and return its position
#    syntax: a_tuple.index(value)
print(f'position of 5 in num_tuple : {num_tuple.index(5)}'
    f'\nposition of 8 in num_tuple : {num_tuple.index(8)}'
    '\n')
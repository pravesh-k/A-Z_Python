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


# 1. Defining a list

# creating an empty list
empty_list_1 = []
empty_list_2 = list()

# list with all items having type int
prime_num_list = [5, 2, 3, 11, 7]
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
    '\nlist_of_lists:\n', list_of_lists
    )


# 3. Accessing items from list

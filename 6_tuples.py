# Tuples in Python: A Tuple is a collection of Python objects separated by commas. 
                # In someways a tuple is similar to a list in terms of indexing, 
                # nested objects and repetition but a tuple is immutable unlike
                # lists which are mutable.


# # Contents:
#   1. Creating tuples


# 1. Creating tuples

# empty tuple
empty_tuple_1 = ()
empty_tuple_2 = tuple()

# tuple with one element
# one_ele_tuple = (1)   # This will create an int type variable
one_ele_tuple_1 = (1,)    # This definition with comma creates a tuple
one_ele_tuple_2 = tuple((1,))

# tuple with all items having type int
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

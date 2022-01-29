# Sets in Python: A Set is an UNORDERED collection data type that is ITERABLE, 
#               MUTABLE and has NO DUPLICATE ELEMENT. Python’s set class 
#               represents the mathematical notion of a set. 
#               The major advantage of using a set, as opposed to a list, is 
#               that it has a highly optimized method for checking whether a 
#               specific element is contained in the set. This is based on a 
#               data structure known as a hash table. 
#               Since sets are unordered, we cannot access items using indexes
#               like we do in lists or sets


# # Contents:
#   1. Creating sets
#   2. Printing sets
#   3. Accessing sets elements


# 1. Creating sets

# empty set
# empty_set_1 = {}      # this defines a dict type and not a set
empty_set_2 = set()

# set with one element
one_ele_set_1 = {1}    
one_ele_set_2 = set((1,))       # passing tuple to a set constructor
one_ele_set_3 = set([1])       # passing list to a set constructor

# set with all items having type int
direction_set = {'east', 'west', 'north', 'south'}      #note no parentheses
prime_num_set = {5, 2, 3, 11, 7, 17, 13}
magic_num_set = set((2, 8, 20, 28, 50))       #note the double parentheses

# set with all items having type string
fruit_set = {"apple", "banana", "cherry", "banana"}

# set with all items having type boolean
bool_set = {True, False, True, True, False}

# set with items having different types
emp_det_set = {'John Walker', 30, 'Manager', 'Sales', 2.55, 98000, True,}

'''
**note 1: Not possible to create set having another sets as items. 
          Raises TypeError: unhasbale type: 'set'
'''

# 2. Printing sets

print(f'empty_set_2 : {empty_set_2}'
    f'\none_ele_set_1 : {one_ele_set_1}'
    f'\none_ele_set_2 : {one_ele_set_2}'
    f'\none_ele_set_3 : {one_ele_set_3}'
    f'\ndirection_set : {direction_set}'
    f'\nprime_num_set : {prime_num_set}'
    f'\nmagic_num_set : {magic_num_set}'
    f'\nfruit_set : {fruit_set}'
    f'\nbool_set : {bool_set}'
    f'\nemp_det_set : {emp_det_set}'
    '\n')


# 3. Accessing set elements
'''
**note 2: It is not possible to access items in a set by referring to an index or  
          a key. This is due to the set being UNORDERED. Due to the same reason, 
          we cannot change the set items but we can add more items to a set and 
          remove items.
'''


# 4. Mutability in sets

# adding items to a set
fruit_set.add('mango')
print(f'fruit_set : {fruit_set}\n')

# adding items from one set to another set
fruit_set_2 = {'dragon-fruit', 'strawberry'}
fruit_set_2.update(fruit_set)
print(f'fruit_set_2 : {fruit_set_2}\n')

# adding items from any iterable to a set
fruit_set_3 = {'dragon-fruit', 'strawberry'}
fruit_set_3.update(['kiwi', 'grapes'])
print(f'fruit_set_3 : {fruit_set_3}\n')

# concatenation is not allowed for sets
# veg_set = {'tomato', 'carrot'} + {'pumpkin', 'onion'}  #Raises TypeError: 
                                                         # unsupported operand type

# removing set items
fruit_set_2.remove('dragon-fruit')
print(f'fruit_set_2 : {fruit_set_2}\n')

fruit_set_2.discard('cherry')
print(f'fruit_set_2 : {fruit_set_2}\n')

'''
**note 3: Difference between remove() and discard() methods.
          discard() method removes the element from the set only if the element is present in the set. If the element is not present in the set, then no error or exception is raised, whereas
          remove() method removes the element from the set only if the element is present in the set, just as the discard() method does but If the element is not present in the set, then an error or exception is raised
'''


# 5. Methods of Sets
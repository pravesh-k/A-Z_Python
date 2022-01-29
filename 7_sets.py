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

# 1. Adds an element to the set
#    syntax: a_set.add(value)

'''Refer to line 74 for example'''

# 2. Removes all the elements from the set
#    syntax: a_set.clear()
magic_num_set.clear()
print(f'magic_num_set : {magic_num_set}\n')

# 3. Returns a copy of the set
#    syntax: a_set.copy()
new_set = prime_num_set.copy()
print(f'new_set : {new_set}\n')

# 4. Returns a set containing the difference between two or more sets
#    syntax: a_set.difference(b_set)
diff_set_1 = fruit_set.difference(fruit_set_2)
diff_set_2 = fruit_set_2.difference(fruit_set)
print(f'diff_set_1 : {diff_set_1}'
    f'\ndiff_set_2 : {diff_set_2}'
    '\n')

# 5. Removes the items in this set that are also included in another, specified set
#    syntax: a_set.difference_update(b_set)
fruit_set_2.difference_update(fruit_set)
print(f'fruit_set_2 : {fruit_set_2}\n')

# 6. Remove the specified item
#    syntax: a_set.discard(value)

'''Refer to line 96 for example'''

# 7. Returns a set, that is the intersection of two or more other sets
#    syntax: a_set.intersection(set1, set2 ... set_n)
fruit_set_2.add('grapes')
fruit_set_2.add('kiwi')
intersect_set_1 = fruit_set_2.intersection(fruit_set_3)
print(f'intersect_set_1 : {intersect_set_1}\n')

# 8. Removes the items in this set that are not present in other, specified set(s)
#    syntax: a_set.intersection_update(set1, set2 ... set_n)
fruit_set_2.intersection(fruit_set_3)
print(f'fruit_set_2 : {fruit_set_2}\n')

# 9. Returns whether two sets have a intersection or not
#    syntax: a_set.isdisjoint(b_set)
#    If returns True: sets are disjoint, meaning no intersection present
#    If returns False: sets are not disjoint, meaning intersection present
print(f'fruit_set_2.isdisjoint(fruit_set_3) :{fruit_set_2.isdisjoint(fruit_set_3)}'
    f'\nfruit_set.isdisjoint(fruit_set_3) :{fruit_set.isdisjoint(fruit_set_3)}'
    '\n')


# 10. Returns whether another set contains this set or not
#     syntax: a_set.issubset(b_set)
print(f'fruit_set_2.issubset(fruit_set_3) :{fruit_set_2.issubset(fruit_set_3)}'
    f'\nfruit_set_3.issubset(fruit_set_2) :{fruit_set_3.issubset(fruit_set_2)}'
    '\n')

# 11. Returns whether this set contains another set or not
#     syntax: a_set.issuperset(b_set)
print(f'fruit_set_2.issuperset(fruit_set_3) :{fruit_set_2.issuperset(fruit_set_3)}'
    f'\nfruit_set_3.issuperset(fruit_set_2) :{fruit_set_3.issuperset(fruit_set_2)}'
    '\n')

# 12. Removes last element from the set.
#     syntax: a_set.pop()
#     Note that sets are UNORDERED so expected item may not get popped out
last_fruit = fruit_set.pop()
print(f'last_fruit : {last_fruit}'
    f'\nfruit_set : {fruit_set}'
    '\n')

# 13. Removes the specified element
#     syntax: a_set.remove(value)

'''Refer to line 92 for example'''

# 14. Returns a set that contains all items from both set, but not the items that
#     are present in both sets.
#     syntax: a_set.symmetric_difference(b_set)
sym_set_1 = fruit_set_3.symmetric_difference(fruit_set_2)
sym_set_2 = fruit_set_2.symmetric_difference(fruit_set_3)
print(f'sym_set_1 : {sym_set_1}'
    f'\nsym_set_2 : {sym_set_2}'
    '\n')

# 15. Update this set with the symmetric differences from this set and another
#     syntax: a_set.symmetric_difference_update(b_set)
fruit_set_3.symmetric_difference_update(fruit_set_2)
print(f'fruit_set_3 : {fruit_set_3}\n')

# 16. Return a set that contains all items from the original set, and all items
#     from the specified set(s).
#     syntax: a_set.union(set1, set2, ..., setn)
union_set = fruit_set.union(fruit_set_2, fruit_set_3)
print(f'union_set : {union_set}\n')

# 17. updates the current set, by adding items from another set (or any other 
#     iterable).
#     syntax: a_set.update(b_set)

'''Refer to line 78 for example'''
'''
Python is a multi-paradigm programming language which means that it supports different 
approaches of programming. And OOPs is one of them.
'''


# OOPs: Object Oriented Programming. This pradigm of programming is based on "Objects".
#       OOPs aims to implement real-world entities like inheritance, hiding, 
#       polymorphism, etc in programming.

# Object: In real world object is anything which is tangible and relatively stable. 
#         Similarly in programming, objects are the interpretation of real world    
#         objects and they posses some attributes and behaviour. Where, we refer 
#         attributes as the data part of the object and behaviour as the methods 
#         of the object.

# Class: Collection of objects is called class. It is a logical entity. A class can 
#        also be defined as a blueprint from which an individual object can be created. 
#        Class doesn't consume any space.


# # Contents:
#   1. Creating Classes
#   2. Creating Objects
#   3. Class Attributes
#   4. Class Methods
#   5. Constructors


# 1. Creating Classes
# Classes can be created using the 'class' keyword.

# Example 1: Creating a class to act as a blueprint for Mammals
class Mammal:
    pass
    # this class has no attributes and no methods

print(f'Passing Class name as an argument in print function output\'s\n{Mammal}\n')

# 2. Creating Objects (using class Mammal)
# Example 1: Creating an object named whale using the Mammal class
whale = Mammal()
print(f'Passing Object name as an argument to print function, output\'s\n{whale}'
    f'\nClass type of whale: {type(whale)}'
    f'\nid of whale: {id(whale)}'
    '\n')

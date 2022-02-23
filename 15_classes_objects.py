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

print(f'Passing Class name as an argument in print function output\'s\n{Mammal}\n'
    # f'\nAttributes of class Mammal:\n{dir(Mammal)}'
    '\n')

# 2. Creating Objects (using class Mammal)
# Example 1: Creating an object named whale using the Mammal class
whale = Mammal()
print(f'Passing Object name as an argument to print function, output\'s\n{whale}'
    f'\nClass type of whale: {type(whale)}'
    f'\nid of whale: {id(whale)}'
    # f'\n\nAttributes of whale: {dir(whale)}'
    f'\n\nMammal class and whale object has same attributes?:\t{dir(Mammal) == dir(whale)}'
    '\n')


# 3. Class Atrributes
# Example 1: Creating a class named Server with attributes
class Server:
    no_vcpu = 4
    ram_capacity = 8
    storage = 50
    # this class has attributes but no methods

print(f'Attributes of Server Class:\n{dir(Server)}'
    f'\n\nMammal and Server class has same attributes?:\t{dir(Mammal) == dir(Server)}'
    f'\n\ndifference in attributes of Mammal and Server class?:\n{list(set(dir(Mammal)) - set(dir(Server))) + list(set(dir(Server)) - set(dir(Mammal)))}'
    '\n')

# Example 2: Creating object from Server and accessing values of object attributes
medium = Server()
print(f'Mammal class and whale object has same attributes?:\t{dir(Server) == dir(medium)}'
    f'\nvalue of no_vcpu attribute of medium object: {medium.no_vcpu}'
    f'\nvalue of ram_capacity attribute of medium object: {medium.ram_capacity}'
    f'\nvalue of storage attribute of medium object: {medium.storage}'
    '\n')

# Example 3: Changing value of attributes of object.
medium.no_vcpu = 6
print(f'value of no_vcpu attribute of medium object: {medium.no_vcpu}\n')
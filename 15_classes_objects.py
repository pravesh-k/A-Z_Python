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
#            Object attributes can be accessed using dot (.) notation.
#            such as: object_name.attribute_name
medium = Server()
print(f'Mammal class and whale object has same attributes?:\t{dir(Server) == dir(medium)}'
    f'\nvalue of no_vcpu attribute of medium object: {medium.no_vcpu}'
    f'\nvalue of ram_capacity attribute of medium object: {medium.ram_capacity}'
    f'\nvalue of storage attribute of medium object: {medium.storage}'
    '\n')

# Example 3: Changing value of attributes of object.
medium.no_vcpu = 6
print(f'value of no_vcpu attribute of medium object: {medium.no_vcpu}\n')


# 4. Class Methods
'''
**note 1:
The 'self' parameter is a reference to the current instance of the class, and is 
used to access the attributes and methods of the class in python. It binds the 
attributes with the given arguments.
'''
# Example 1:
class Human:
    # Attributes of Human
    ear_count = 2
    nose_count = 1
    eye_count = 2
    leg_count = 2
    hand_count = 2
    finger_count = 20

    # Methods/Behaviour of Human
    def walk(self):
        print(f'Walk with {self.leg_count} legs\n')
    
    def cook(self):
        print(f'Cooks using {self.hand_count} hands\n')

    # a class can also contain methods only.


# Creating object of Human class
john = Human()
john.walk()
john.cook()


# 5. Constructor
'''
**note 2:
Constructors are generally used for instantiating an object. The task of constructors 
is to initialize(assign values) to the data members of the class when an object of 
the class is created. In Python the __init__() method is called the constructor and 
is always called when an object is created.

In other words, __init__() function can be used to assign values to object properties, 
or other operations that are necessary to do when the object is being created.
'''

# Example 1:
class Dog:
    
    # class attribute
    leg_count = 4

    # instance attribute, note that usage of self keyword for defining instance 
    # attributes but not for class attribute
    def __init__(self):
        self.color = 'Black'
        self.height = 'Medium'

tony = Dog()
# while creating an object using constructor, argument for self parameter is not required
print(f'tony.leg_count: {tony.leg_count}'
    f'\ntony.color: {tony.color}'
    f'\ntony.height: {tony.height}'
    '\n')


'''
**note 3:
Class Attributes vs Instance Attributes:
Class attributes are the variables defined directly in the class that are shared by all 
objects of the class. Instance attributes are attributes or properties attached to an 
instance of a class. Instance attributes are defined in the constructor.

Class attributes can be accessed via using class.attribute notation as well as
object.attribute notation but instance attribute can only be accessed via object.attribute
notation.

Changing value of class attribute via class.attribute=value will be reflected to all the
objects but changing value of instance attribute will not be reflected in other objects of
same class.
'''

# Example 2:
class Example:
    
    count_1 = 0
    count_2 = 0

    def __init__(self):
        Example.count_1 += 1
        self.count_2 += 5


obj1 = Example()
print(f'obj1.count_1: {obj1.count_1}\t\tobj1.count_2: {obj1.count_2}')
obj2 = Example()
print(f'obj2.count_1: {obj2.count_1}\t\tobj2.count_2: {obj2.count_2}')
obj3 = Example()
print(f'obj3.count_1: {obj3.count_1}\t\tobj3.count_2: {obj3.count_2}\n')

# Observation: when count_1 class attribute is changed using classname.attribute, the change
# is visible through out the class objects, even the objects created further will reflect the
# change. While the count_2 class attribute when accessed and modified using objectname.
# attribute, the changed value is not reflected throughout the class objects, rather count_2 
# is initialized each time.
# The class attribute can be accessed anywhere in the program using classname.attribute 
# notation

# Example 3: Parameterized constructors (the above examples do not require any arguments while 
# creating an object since the __init__() method does not ask for any parameter). 
# An __init__() can accept arguments as normally as a parameterized function can accept.

class Cellphone:
    
    def __init__(self, brand, screensize, os, ram, storage=128):        
        #default parameter storage
        self.brand = brand
        self.screensize = screensize
        self.os = os
        self.ram = ram
        self.storage = storage

cell_1 = Cellphone('OnePlus', '6.3 inches', 'Android 12', 6, 64) # overriding default storage
print(f'attribute of cell_1 in dict form:\n{vars(cell_1)}\n')

cell_2 = Cellphone('Iphone', '5.8 inches', 'IOS 13', 8) # keeping default storage
print(f'attribute of cell_2 in dict form:\n{vars(cell_2)}\n')
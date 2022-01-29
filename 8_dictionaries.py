# Dictionary: It is an ORDERED(only after Python3.7 release) collection of data 
#             values, used to store data values like a map, which, unlike other 
#             data types that hold only a single value as an element, Dictionary 
#             holds KEY:VALUE pair. Key-value is provided in the dictionary to 
#             make it more optimized.
#             Dictionary is MUTABLE and ITERABLE.
#             *Note: Keys in a dictionary don’t allow Polymorphism.


# # Contents:
#   1. Creating a dictionary

# 1. Creating a dictionary

'''
**note 1: Dictionary can be created by placing a sequence of elements within 
          curly {} braces, separated by 'comma'. Dictionary holds pairs of values, 
          one being the KEY and the other corresponding pair element being its 
          VALUE. Values in a dictionary can be of any data type and can be 
          duplicated, whereas keys can't be repeated and can't be duplicated. 
'''

# empty dictionary
empty_dict_1 = {}
empty_dict_2 = dict()

# dictionary with multiple key value pairs and values of different data types
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": ['Red', 'Blue', 'White'],
    "EV": False
    }

# creating dictionary using constructor
emp_dict = dict([
    ['name', 'Adam'], 
    {'exp', 6}, 
    ('dept', 'Sales'), 
    ('designation', 'Lead')
    ])

# creating nested dictionary
student_dict = {
    'name': 'John',
    'roll': 34,
    'class': 8,
    'books_issued': {
        'english': {
            'language': 1,
            'literature': 2
            },
        'maths': 1,
        'social': 3,
        'science': 3
        },
    'section': 'B'
    }

# 2. Printing dictionaries

print(f'empty_dict_1 : {empty_dict_1}\n'
    f'\nempty_dict_2 : {empty_dict_2}\n'
    f'\ncar_dict : {car_dict}\n'
    f'\nemp_dict : {emp_dict}\n'
    f'\nstudent_dict : {student_dict}\n'
    '\n')

# 3. Accessing dictionary items

# a. Access the items of a dictionary by referring to its key name, inside square brackets
print(f'\ncar_dict["year"] : {car_dict["year"]}\n'
    f'\ncar_dict["color"] : {car_dict["color"]}\n'
    f'\nstudent_dict["books_issued"] : {student_dict["books_issued"]}\n'
    f'\nstudent_dict["books_issued"]["english"] : {student_dict["books_issued"]["english"]}\n'
    f'\nstudent_dict["books_issued"]["english"]["literature"] : {student_dict["books_issued"]["english"]["literature"]}\n'
    '\n')


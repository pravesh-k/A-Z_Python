# Dictionary: It is an ORDERED(only after Python3.7 release) collection of data 
#             values, used to store data values like a map, which, unlike other 
#             data types that hold only a single value as an element, Dictionary 
#             holds KEY:VALUE pair. Key-value is provided in the dictionary to 
#             make it more optimized.
#             Dictionary is MUTABLE and ITERABLE.
#             *Note: Keys in a dictionary don’t allow Polymorphism.


# # Contents:
#   1. Creating a dictionary
#   2. Printing dictionaries
#   3. Accessing dictionary items
#   4. Changing values of keys
#   5. Adding items to the dictionary

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

# b. Accessing value of the item with the specified key using get() method.
#    syntax: a_dict.get(key, value)
#            where value argument is optional and is useful when the key doesn't 
#            exist in the dict, so the get() method returns the value argument
#    This method returns the value associated to the key passed to the get() method

car_color = car_dict.get('color')
print(f'car_color : {car_color}\n')

car_brand = car_dict.get('brand', 'Honda')      
# here 'Honda' is passed to value but it won't populate on output because brand 
# key exists in the car_dict dictionary
print(f'car_brand : {car_brand}\n')

car_supply = car_dict.get('supply', False)
# here 'False' is passed to value and it will be returned because key supply 
# doesn't exists in the car_dict dictionary
print(f'car_supply : {car_supply}\n')

car_body = car_dict.get('body')
# here 'body' is passed as key but it is originally not present in the car_dict. 
# By default 'None' is passed to the value argument of get() method, and so this 
# get query will return None.
print(f'car_body : {car_body}\n')

# c. Accessing all the keys of the dictionary using keys() method.
#    syntax: a_dict.keys()
#    This method returns the view object. The view object contains the keys of the 
#    dictionary, as a list.
#    The view object will reflect any changes (add item, remove item) done to the
#    dictionary.

car_key_list = car_dict.keys()
print(f'car_key_list : {car_key_list}\n')

# d. Accessing all the values of the dictionary using values() method.
#    syntax: a_dict.values()
#    This method returns the view object. The view object contains the values of 
#    the dictionary, as a list.
#    The view object will reflect any changes (add item, update value, remove 
#    item) done to the dictionary.

car_value_list = car_dict.values()
print(f'car_value_list : {car_value_list}\n')

# e. Accessing all the items of the dictionary using items() method.
#    syntax: a_dict.items()
#    This method returns the view object. The view object contains the key-value 
#    pairs of the dictionary, as tuples in a list.
#    The view object will reflect any changes (add item, update value, remove 
#    item) done to the dictionary.

car_item_list = car_dict.items()
print(f'car_item_list : {car_item_list}\n')


# 4. Changing values of keys

# a. Changing the value of a specific item by referring to its key name.
student_dict['name'] = 'Steve'
student_dict['roll'] = 10
student_dict['books_issued']['maths'] = 2
student_dict['books_issued']['english']['language'] = 2
print(f'student_dict : {student_dict}\n')

# b. Using update() method to change the value of a key
#    syntax: a_dict.update(iterable)
#            where iterable a dictionary or an iterable object with key value 
#            pairs, that will be inserted to the dictionary
#    If the key provided in the iterable passed to the method isn't present in the 
#    dict originally then it adds that item to the dict

car_dict.update({'year': 1999})
car_dict.update([('wheel_type', 'Alloy')])
print(f'car_dict : {car_dict}\n')
student_dict['books_issued'].update({'social': 1})
print(f'student_dict : {student_dict}\n')


# 5. Adding items to the dictionary

# a. Add an item using a new index key and assigning a value to it.
car_dict['seat_capacity'] = 5
car_dict['vehicle_category'] = 'SUV'
print(f'car_dict : {car_dict}\n')

# b. Using update method to add new key-value pair to the dictionary
'''Example of this operation is demonstrated in line 157'''


# 6. 
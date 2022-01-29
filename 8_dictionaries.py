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
super_car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": ['Red', 'Blue', 'White'],
    "EV": False
    }

# 2. Printing dictionaries

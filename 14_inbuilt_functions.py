# The Python interpreter has a number of functions and types built into it that 
# are always available.

# They are listed here in alphabetical order.

# 1. abs()
'''
This function returns the absolute value of the given number. If the number is 
a complex number, abs() returns its magnitude.
syntax:
abs(num)
where num can be integer, float and complex number
'''
# Example 1:
from statistics import mode
from unittest.mock import sentinel
from numpy import byte, source


num1 = -20
num2 = -33.33
c_num = 5+4j
print(f'absolute value of {num1} is {abs(num1)}'
    f'\nabsolute value of {num2} is {abs(num2)}'
    f'\nmagnitude value of {c_num} is {abs(c_num)}'
    '\n')


# 2. any()
'''
This function returns True if any element of an iterable is True. If not, it 
returns False.
syntax:
any(iterable)
'''
# Example 1:
l1 = [1, 2, 4, 0]
l2 = 0, 0, 0
l3 = [True, True, False, True]
l4 = ['a', 'b', False, 0]
l5 = 0, False
l6 = []
l7 = '000'

print(f'any(l1) where l1= {l1} returns {any(l1)}'
    f'\nany(l2) where l2= {l2} returns {any(l2)}'
    f'\nany(l3) where l3= {l3} returns {any(l3)}'
    f'\nany(l4) where l4= {l4} returns {any(l4)}'
    f'\nany(l5) where l5= {l5} returns {any(l5)}'
    f'\nany(l6) where l6= {l6} returns {any(l6)}'
    f'\nany(l7) where l7= {l7} returns {any(l7)}'
    '\n')


# 3. all()
'''
This function returns True if all elements in the given iterable are true. If 
not, it returns False.
syntax:
all(iterable)
'''
# Example 1: Using the variables from section 2

print(f'all(l1) where l1= {l1} returns {all(l1)}'
    f'\nall(l2) where l2= {l2} returns {all(l2)}'
    f'\nall(l3) where l3= {l3} returns {all(l3)}'
    f'\nall(l4) where l4= {l4} returns {all(l4)}'
    f'\nall(l5) where l5= {l5} returns {all(l5)}'
    f'\nall(l6) where l6= {l6} returns {all(l6)}'
    f'\nall(l7) where l7= {l7} returns {all(l7)}'
    '\n')


# 4. ascii()
# This function returns a string containing a printable representation of an 
# object. It escapes the non-ASCII characters in the string using \x, \u or \U 
# escapes.
'''
syntax:
all(object)
where the object can be string, list, etc
'''
# Example 1:
normal_text = 'Python is interesting'
other_text = 'Pythön is interesting'

print(f'{normal_text} when passed to ascii() returns: {ascii(normal_text)}'
    f'\n{other_text} when passed to ascii() returns: {ascii(other_text)}'
    '\n')


# 5. bin()
'''
This function converts and returns the binary equivalent string of a given 
integer (even represented in octal or hex number).
syntax:
bin(num)
'''
# Example 1:
d_num = 5
o_num = 0o12
h_num = 0x16
print(f'The binary equivalent of {d_num} is: {bin(d_num)}'
    f'\nThe binary equivalent of {o_num} is: {bin(o_num)}'
    f'\nThe binary equivalent of {h_num} is: {bin(h_num)}'
    '\n')


# 6. bool()
'''
This function converts a value to Boolean (True or False) using the standard 
truth testing procedure.
syntax:
bool(value)
'''
# Example 1:
val1 = None
val2 = True
val3 = 'string'
val4 = []
val5 = [0]
val6 = [1, 3, 4]

print(f'The bool equivalent of {val1} is: {bool(val1)}'
    f'\nThe bool equivalent of {val2} is: {bool(val2)}'
    f'\nThe bool equivalent of {val3} is: {bool(val3)}'
    f'\nThe bool equivalent of {val4} is: {bool(val4)}'
    f'\nThe bool equivalent of {val5} is: {bool(val5)}'
    f'\nThe bool equivalent of {val6} is: {bool(val6)}'
    '\n')


# 7. bytearray()
'''
This function method returns a bytearray object which is an array of the given bytes.
syntax:
bytearray(source, encoding, error)
'''
# Example 1:
prime_list = [2, 3, 5, 7]
welcome_msg = 'Lorem Ipsum!'
num3 = 5
prime_byte_array = bytearray(prime_list)
welcome_byte_array = bytearray(welcome_msg, encoding='utf-8')
byte_array_num3 = bytearray(num3)

print(f'byte array of list: {prime_list} is: {prime_byte_array}'
    f'\nbyte array of string: {welcome_msg} is: {welcome_byte_array}'
    f'\nbyte array of number: {num3} is: {byte_array_num3}'
    '\n')


# 8. bytes()
'''
This function method returns an immutable bytes object initialized with the 
given size and data.
syntax:
bytes(source, encoding, error)
'''
# Example 1:
odd_list = [1, 3, 5, 7, 9]
msg_1 = 'Python is awesome!'
num4 = 4
odd_bytes = bytes(odd_list)
msg_1_bytes = bytes(msg_1, encoding='utf-8')
num4_bytes = bytes(num4)

print(f'bytes of list: {odd_list} is: {odd_bytes}'
    f'\nbytes of string: {msg_1} is: {msg_1_bytes}'
    f'\nbytes of number: {num4} is: {num4_bytes}'
    '\n')


# 9. chr()
'''
This function returns a character (a string) from an integer (represents unicode 
code point of the character).
syntax:
chr(i), where i is an integer
'''
# Example 1:
print(f'chr(65) is {chr(65)}'
    f'\nchr(98) is {chr(98)}'
    f'\nchr(2000) is {chr(2000)}'
    # f'\nchr(-1) is {chr(-1)}'     # ValueError, positive integers are required
    '\n')


# 10. compile()
'''
This function returns a Python code object from the source (normal string, a byte 
string, or an AST object).
compile() method is used if the Python code is in string form or is an AST object, 
and it needs to be changed to a code object.
The code object returned by compile() method can later be called using methods 
like: exec() and eval() which will execute dynamically generated Python code.

syntax:
compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
'''
# Example 1:
code_string = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
code_from_string = compile(source=code_string, filename='summation', mode='exec')
print(f'code object from the string is: {code_from_string} and it evaluates to')
exec(code_from_string)


# 11. classmethod()
'''
This function returns a class method for the given function. A class method is a 
method that is bound to a class rather than its object.
This function usage is deprecated and is non-pythonic instead @classmethod 
decorator should be used. Refer to the decorators file.
'''

# 12. complex()
'''
This function returns a complex number when real and imaginary parts are provided, 
or it converts a string to a complex number.
syntax:
complex(real, imag) 
OR
complex('real+imag')
'''
# Example 1:
cmplx_1 = complex(4, 5)
cmplx_2 = complex('2-3j')
cmplx_3 = complex(7)
cmplx_4 = complex()
cmplx_5 = complex('0-1.5J')

print(f'cmplx_1: {cmplx_1}'
    f'\ncmplx_2: {cmplx_2}'
    f'\ncmplx_3: {cmplx_3}'
    f'\ncmplx_4: {cmplx_4}'
    f'\ncmplx_5: {cmplx_5}'
    '\n')


# 13. dict()
'''
The dict() constructor creates a dictionary in Python. Refer to dictionaries file.
'''


# 14. dir()
'''
This function tries to return a list of valid attributes of any object.
syntax:
dir(object)
'''
# Example 1:
even_list = [2, 4, 6, 8]
emp_dict = dict(name='Jacob', des='Manager', salary=50000)
num_5 = 5000
print(f'attributes of {even_list} are\n\n{dir(even_list)}\n'
    f'\nattributes of {emp_dict} are\n\n{dir(emp_dict)}\n'
    f'\nattributes of {num_5} are\n\n{dir(num_5)}\n'
    '\n')


# 15. divmod()
'''
This function takes two numbers and returns a pair of numbers (a tuple) consisting 
of their quotient and remainder.
syntax:
divmod(numerator, denominator)
'''
# Example 1:
print(f'divmod(8, 3) = {divmod(8, 3)}'
    f'\ndivmod(3, 8) = {divmod(3, 8)}'
    f'\ndivmod(5, 5) = {divmod(5, 5)}'
    f'\ndivmod(8.0, 3) = {divmod(8.0, 3)}'
    f'\ndivmod(3, 8.0) = {divmod(3, 8.0)}'
    f'\ndivmod(7.5, 2.5) = {divmod(7.5, 2.5)}'
    f'\ndivmod(2.6, 0.5) = {divmod(2.6, 0.5)}'
    '\n')


# 16. enumerate()
'''
This function adds a counter to an iterable and returns it (the enumerate object).
syntax:
enumerate(iterable, start)
where, start parameter is optional and default value is 0
'''
# Example 1:
grocery = ['bread', 'milk', 'butter']
enumerate_grocery_1 = enumerate(grocery)
enumerate_grocery_2 = enumerate(grocery, 5)

print(f'type of enumerate_grocery: {type(enumerate_grocery_1)}'
    f'\nenumerate_grocery_1: {enumerate_grocery_1}'
    f'\ncasting to list: {list(enumerate_grocery_1)}'
    f'\nchanging default counter: {list(enumerate_grocery_2)}'
    '\n')

# Example 2: looping over an enumerate object
for count, item in enumerate(grocery):
    print(count, item)
print()


# 17. staticmethod()
'''
This built-in function returns a static method for a given function.

Static methods, much like class methods, are methods that are bound to a class 
rather than its object.
They do not require a class instance creation. So, they are not dependent on the 
state of the object.
The difference between a static method and a class method is Static method knows 
nothing about the class and just deals with the parameters. Whereas, Class method 
works with the class since its parameter is always the class itself.

staticmethod() is considered a un-Pythonic way of creating a static function. 
Hence, in newer versions of Python, @staticmethod decorator should be used.
'''


# 18. filter()
'''
The filter() function extracts elements from an iterable (list, tuple etc.) for 
which a function returns True.
syntax:
filter(function, iterable)
Refer to lambda_recursion file for example.
'''


# 19. eval()
'''
This function parses the expression passed to this method and runs python expression 
(code) within the program.
syntax:
eval(expression, globals, locals)
where, globals and locals parameter are optional where these variables are used for 
global and local variables respectively.
'''
# Example 1:
num_6 = 8
square_num = eval('num_6**2')
print(f'square_num: {square_num}\n')


# 20. float()
'''
This function returns a floating point number from a number or a string.
syntax:
float(int or string)
Refer to numerics.py file for example (section 3)
'''


# 21. format()
'''
This function returns a formatted representation of the given value controlled by the 
format specifier.
syntax:
format(value format_spec)
Refer to strings.py file for examples (section 6)
'''


# 22. frozenset()
'''
This function returns an immutable frozenset object initialized with elements from the 
given iterable.
syntax:
frozenset([iterable])
where iterable is optional
Refer to sets.py file (section 6) for examples
'''


# 23. exec()
'''
This function executes the dynamically created program, which is either a string or a 
code object.
syntax:
exec(object, globals, locals)
Refer to section 10 for examples on exec
'''


# 24. hasattr()
'''
This function returns true if an object has the given named attribute and false if it 
does not.
syntax:
hasattr(object, name)
'''
# Example 1:
car_list = ['BMW', 'Benz', 'Honda', 'Porsche']
print(f'is count an attribute of car_list? :{hasattr(car_list, "count")}\n')


# 25. help()
'''
This function calls the inbuilt python help system
syntax:
help(object)
where object is optional
'''
# Example 1:
# help(list)


# 26. hex()
'''
This function converts an integer number to the corresponding hexadecimal string.
syntax:
hex(value)
where value can be integer

Other implemetation: for converting float types
float.hex(value)
'''
# Example 1:
b_num = 0b0111
o_num = 0o12
d_num = 16
print(f'The hex equivalent of {b_num} is: {hex(b_num)}'
    f'\nThe hex equivalent of {o_num} is: {hex(o_num)}'
    f'\nThe hex equivalent of {d_num} is: {hex(d_num)}'
    '\n')

# Example 2:
f_num = 16.15
print(f'The hex equivalent of {f_num} is: {float.hex(f_num)}'
    '\n')


# 27. hash()
'''
This function returns the hash value of an object if it has one. Hash values are just 
integers that are used to compare dictionary keys during a dictionary look quickly.

A hash value is a numeric value of a fixed length that uniquely identifies data.
syntax:
hash(object)
'''
message_1 = 'Welcome here!'
num_7 = 3121
f_num_2 = 12.12
print(f'hash value of message_1: {hash(message_1)}'
    f'\nhash value of num_7: {hash(num_7)}'
    f'\nhash value of f_num_2: {hash(f_num_2)}'
    '\n')


# 28. input()
'''
This function takes input from the user and returns it. This always returns a string.
This essentially is the most important and most used input method in python3.
syntax:
input(prompt_message)
where prompt message is optional
'''
# Example 1:
# input_1 = input()
# input_2 = input('enter a value ')
# print(f'value of input_1: {input_1}'
#     f'\nvalue of input_2: {input_2}'
#     '\n')


# 29. id()
'''
This function returns identity/memory address (unique integer) of an object.
syntax:
id(object)
Refer to lists.py (**note 1) for examples
'''


# 30. isinstance()
'''
This function checks if the object (first argument) is an instance or subclass of 
classinfo class (second argument).
syntax:
isinstance(object, classinfo)
'''
# Example 1:
numbers = [15, 5, 8, 3, 10]
print(f'is numbers an instance of list?: {isinstance(numbers, list)}'
    f'\nis numbers an instance of dict?: {isinstance(numbers, dict)}'
    '\n')

# Example 2: passing a tuple of classinfo
fruits = 'kiwi', 'mango'
print(f'is fruits an instance of either list or tuple or dict?: '
    f'{isinstance(fruits, (list, tuple, dict))}'
    '\n')


# 31. int()
'''
This function returns an integer object from any number or string
syntax:
int(x, base)
where x is the number or string and base of x
'''
# Example 1:
print(f'int(50): {int(50)}'
    f'\nint("100"): {int("100")}'
    f'\nint("0b1100", 2): {int("0b1100", 2)}'
    f'\nint("0o105", 8): {int("0o105", 8)}'
    f'\nint(123.123): {int(123.123)}'
    f'\nint("50", 10): {int("50", 10)}'
    '\n')


# 32. issubclass()
'''
This function checks if the class argument (first argument) is a 
subclass of classinfo class (second argument).
syntax:
issubclass(class, classinfo)
where class is that which needs to be checked whether it is a subclass 
of classinfo
'''
# Example 1:
class A:
    pass
class B(A):
    pass

print(f'is B a subclass of A? : {issubclass(B, A)}'
    f'\nis A a subclass of A? : {issubclass(A, A)}'
    f'\nis A a subclass of B? : {issubclass(A, B)}'
    '\n')


# 33. iter()
'''
This function returns an iterator for the given object.

**note 1: an iterator is an object which implements the iterator protocol, 
which means it consists of the methods such as __iter__() and __next__(). 
An iterator is an iterable object with a state so it remembers where it is
during iteration

syntax:
iter(object, sentinel)
where object indicates the object whose iterable needs to be created
and sentinel is optional which is used to indicate the end of the sequence
The values out of an iterable can be accessed via attribute __next__()
'''
# Example 1:
vowels = ['a', 'b', 'c', 'd', 'e']
vowels_iter = iter(vowels)
# print(f'attributes of vowels_iter: {dir(vowels_iter)}\n')
print(f'vowels_iter.__next__(): {vowels_iter.__next__()}'
    f'\nvowels_iter.__next__(): {vowels_iter.__next__()}'
    f'\nvowels_iter.__next__(): {vowels_iter.__next__()}'
    '\n')


# 34. list()
'''
The list() constructor returns a list in python.
syntax:
list(iterable)
where iterable is optional
Refer to lists.py file for examples
'''


# 35. len()
'''
This function returns the number of items (length) in an object.
syntax:
len(sequence)
'''
# Example 1:
list_1 = []
list_2 = [1, 1, 8, 8]
tuple_1 = 2, 5, 7, 11, 17
dict_1 = {'a':1, 'b':2}
string_1 = 'Okaayyy'
print(f'length of list_1: {list_1} is= {len(list_1)}'
    f'\nlength of list_2: {list_2} is= {len(list_2)}'
    f'\nlength of tuple_1: {tuple_1} is= {len(tuple_1)}'
    f'\nlength of dict_1: {dict_1} is= {len(dict_1)}'
    f'\nlength of string_1: {string_1} is= {len(string_1)}'
    '\n')


# 36. max()
'''
This function returns the largest item in an iterable. It can also be 
used to find the largest item between two or more parameters.
syntax:
max(iterable, *iterables, key, default)
where there can be a single or multiple iterable,
key is optional and accepts a function where the iterables are 
passed and comparison is performed based on its return value. And 
default is also optional which is to be returned when iterable is empty
'''
# Example 1:
marks = 15, 20, 7, 98, 45
cities = 'kolkata', 'mumbai', 'delhi', 'bangalore'
subject_credit = {'physics':3, 'maths':4, 'chemistry':3, 'english':1}
print(f'max in marks: {max(marks)}'
    f'\nmax in cities: {max(cities)}'
    f'\nmax in cities: {max(cities, key=len)}'
    f'\nsubject with max in subject_credit: {max(subject_credit, key=lambda i: subject_credit[i])}'
    '\n')


# 37. min()
'''
This function returns the smallest item in an iterable. It can also be 
used to find the smallest item between two or more parameters.
syntax:
min(iterable, *iterables, key, default)
where there can be a single or multiple iterable,
key is optional and accepts a function where the iterables are 
passed and comparison is performed based on its return value. And 
default is also optional which is to be returned when iterable is empty
'''
# Example 1:
print(f'min in marks: {min(marks)}'
    f'\nmin in cities: {min(cities)}'
    f'\nmin in cities: {min(cities, key=len)}'
    f'\nsubject with min in subject_credit: {min(subject_credit, key=lambda i: subject_credit[i])}'
    f'\nmin in empty list: {min(list(), default=None)}'
    '\n')


# 38. map()
'''
This function applies a given function to each item of an iterable (list, tuple 
etc.) and returns an iterator.
syntax:
map(function, iterable)
*more than one iterable can be passed at once to the function.
Refer to lambda_recursion file (section 2) for examples
'''


# 39. object()
'''
This function returns a featureless object which is a base for all classes.
syntax:
object()
'''
test_object = object()
print(f'test_object: {test_object}'
    f'\n\nattributes of test_object:\n {dir(test_object)}'
    '\n')


# 40. oct()
'''
This function takes an integer number (decimal, binary, hexadecimal) and returns 
its octal representation.
syntax:
oct(num)
'''
print(f'oct(10) is: {oct(10)}'
    f'\noct(0b101) is: {oct(0b101)}'
    f'\noct(0XA) is: {oct(0XA)}'
    '\n')


# 41. ord()
'''
This function returns an integer representing the Unicode character. This function 
is reverse of chr() function.
syntax:
order(ch)
where ch is a unicode character
'''
print(f'ord("5"): {ord("5")}'
    f'\nord("A"): {ord("A")}'
    f'\nord("$"): {ord("$")}'
    '\n')


# 42. open()
'''
This function opens the file (if possible) and returns the corresponding file 
object.
syntax:
open(file, mode, buffering, encoding, errors, newline, closefd, opener)
where, 
file: filename with path, 
mode: the mode in which file needs to be opened ('r' for read, 'w' for write, etc)
buferring: used for setting buferring policy
encoding: the encoding format
errors: string specifying handling of encoding/decoding erros 
newline: working of newline modes
*All other parameters are optional except file
Refer to file_handling file for examples
'''
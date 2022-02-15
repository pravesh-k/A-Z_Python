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
grocery = ['bread', 'milk', 'butter']
enumerate_grocery_1 = enumerate(grocery)
enumerate_grocery_2 = enumerate(grocery, 5)

print(f'type of enumerate_grocery: {type(enumerate_grocery_1)}'
    f'\nenumerate_grocery_1: {enumerate_grocery_1}'
    f'\ncasting to list: {list(enumerate_grocery_1)}'
    f'\nchanging default counter: {list(enumerate_grocery_2)}'
    '\n')

# looping over an enumerate object
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
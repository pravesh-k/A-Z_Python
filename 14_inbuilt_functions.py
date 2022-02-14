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
    '\n')
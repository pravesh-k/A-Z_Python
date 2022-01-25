# Number data types store numeric values. They are immutable data types, 
# which means that changing the value of a number data type results in a 
# newly allocated object.

# Different types of Number data types are :
#   int
#   float
#   complex

'''
**********************************************************
**note 1: 'type()' in-built function: It returns class type
           of the argument(object) passed as parameter.
example:
x = 10
print(type(x))
**********************************************************
'''

# 1. Creating numeric type variables

int_num_1 = 10
int_num_2 = -15
int_num_3 = 0
int_num_4 = 999999999999999999

float_num_1 = 6.6
float_num_2 = -5.13
float_num_3 = 0.0000000000000000001
float_num_4 = 4/7


complex_num_1 = 1+2j
complex_num_2 = -1+2j
complex_num_3 = -1.5-2j
complex_num_4 = 1-2.56j
complex_num_5 = 1+0j
complex_num_6 = 0+1j
complex_num_7 = 0+0j
complex_num_8 = 1j

print(f'int_num_1\ttype: {type(int_num_1)}\tvalue: {int_num_1}',
    f'\nint_num_2\ttype: {type(int_num_2)}\tvalue: {int_num_2}',
    f'\nint_num_3\ttype: {type(int_num_3)}\tvalue: {int_num_3}',
    f'\nint_num_4\ttype: {type(int_num_4)}\tvalue: {int_num_4}',
    '\n')

print(f'float_num_1\ttype: {type(float_num_1)}\tvalue: {float_num_1}',
    f'\nfloat_num_2\ttype: {type(float_num_2)}\tvalue: {float_num_2}',
    f'\nfloat_num_3\ttype: {type(float_num_3)}\tvalue: {float_num_3}',
    f'\nfloat_num_4\ttype: {type(float_num_4)}\tvalue: {float_num_4}',
    '\n')

print(f'complex_num_1\ttype: {type(complex_num_1)}\tvalue: {complex_num_1}',
    f'\ncomplex_num_2\ttype: {type(complex_num_2)}\tvalue: {complex_num_2}',
    f'\ncomplex_num_3\ttype: {type(complex_num_3)}\tvalue: {complex_num_3}',
    f'\ncomplex_num_4\ttype: {type(complex_num_4)}\tvalue: {complex_num_4}',
    f'\ncomplex_num_5\ttype: {type(complex_num_5)}\tvalue: {complex_num_5}',
    f'\ncomplex_num_6\ttype: {type(complex_num_6)}\tvalue: {complex_num_6}',
    f'\ncomplex_num_7\ttype: {type(complex_num_7)}\tvalue: {complex_num_7}',
    f'\ncomplex_num_8\ttype: {type(complex_num_8)}\tvalue: {complex_num_8}',
    '\n')


# 2. Arithmetic operations between different numeric data types

# a. Addition/Subtraction
int_int_sum = int_num_1 + int_num_2
int_float_sum = int_num_1 + float_num_1
int_cmplx_sum = int_num_1 + complex_num_1
float_float_sum = float_num_1 + float_num_2
float_cmplx_sum = float_num_1 + complex_num_1
cmplx_cmplx_sum = complex_num_1 + complex_num_2

print(f'int_int_sum\ttype: {type(int_int_sum)}\tvalue: {int_int_sum}',
    f'\nint_float_sum\ttype: {type(int_float_sum)}\tvalue: {int_float_sum}',
    f'\nint_cmplx_sum\ttype: {type(int_cmplx_sum)}\tvalue: {int_cmplx_sum}',
    f'\nfloat_float_sum\ttype: {type(float_float_sum)}\tvalue: {float_float_sum}',
    f'\nfloat_cmplx_sum\ttype: {type(float_cmplx_sum)}\tvalue: {float_cmplx_sum}',
    f'\ncmplx_cmplx_sum\ttype: {type(cmplx_cmplx_sum)}\tvalue: {cmplx_cmplx_sum}',
    '\n')

# b. Multiplication
int_int_mul = int_num_1 * int_num_2
int_float_mul = int_num_1 * float_num_1
int_cmplx_mul = int_num_1 * complex_num_1
float_float_mul = float_num_1 * float_num_2
float_cmplx_mul = float_num_1 * complex_num_1
cmplx_cmplx_mul = complex_num_1 * complex_num_2

print(f'int_int_mul\ttype: {type(int_int_mul)}\tvalue: {int_int_mul}',
    f'\nint_float_mul\ttype: {type(int_float_mul)}\tvalue: {int_float_mul}',
    f'\nint_cmplx_mul\ttype: {type(int_cmplx_mul)}\tvalue: {int_cmplx_mul}',
    f'\nfloat_float_mul\ttype: {type(float_float_mul)}\tvalue: {float_float_mul}',
    f'\nfloat_cmplx_mul\ttype: {type(float_cmplx_mul)}\tvalue: {float_cmplx_mul}',
    f'\ncmplx_cmplx_mul\ttype: {type(cmplx_cmplx_mul)}\tvalue: {cmplx_cmplx_mul}',
    '\n')

# c. Division
int_int_div = int_num_1 / int_num_2
int_float_div = int_num_1 / float_num_1
int_cmplx_div = int_num_1 / complex_num_1
float_float_div = float_num_1 / float_num_2
float_cmplx_div = float_num_1 / complex_num_1
cmplx_cmplx_div = complex_num_1 / complex_num_2

print(f'int_int_div\ttype: {type(int_int_div)}\tvalue: {int_int_div}',
    f'\nint_float_div\ttype: {type(int_float_div)}\tvalue: {int_float_div}',
    f'\nint_cmplx_div\ttype: {type(int_cmplx_div)}\tvalue: {int_cmplx_div}',
    f'\nfloat_float_div\ttype: {type(float_float_div)}\tvalue: {float_float_div}',
    f'\nfloat_cmplx_div\ttype: {type(float_cmplx_div)}\tvalue: {float_cmplx_div}',
    f'\ncmplx_cmplx_div\ttype: {type(cmplx_cmplx_div)}\tvalue: {cmplx_cmplx_div}',
    '\n')

# d. Floor Division
int_int_fod = int_num_1 // int_num_2
int_float_fod = int_num_1 // float_num_1
# int_cmplx_fod = int_num_1 // complex_num_1      # Raises TypeError
float_float_fod = float_num_1 // float_num_2
# float_cmplx_fod = float_num_1 // complex_num_1      #Raises TypeError 
# cmplx_cmplx_fod = complex_num_1 // complex_num_2      #Raises TypeError

print(f'int_int_fod\ttype: {type(int_int_fod)}\tvalue: {int_int_fod}',
    f'\nint_float_fod\ttype: {type(int_float_fod)}\tvalue: {int_float_fod}',
    f'\nfloat_float_fod\ttype: {type(float_float_fod)}\tvalue: {float_float_fod}',
    '\n')

# e. Modulus
int_int_mod = int_num_1 % int_num_2
int_float_mod = int_num_1 % float_num_1
# int_cmplx_mod = int_num_1 % complex_num_1      #Raises TypeError
float_float_mod = float_num_1 % float_num_2
# float_cmplx_mod = float_num_1 % complex_num_1      #Raises TypeError
# cmplx_cmplx_mod = complex_num_1 % complex_num_2      #Raises TypeError

print(f'int_int_mod\ttype: {type(int_int_mod)}\tvalue: {int_int_mod}',
    f'\nint_float_mod\ttype: {type(int_float_mod)}\tvalue: {int_float_mod}',
    f'\nfloat_float_mod\ttype: {type(float_float_mod)}\tvalue: {float_float_mod}',
    '\n')

# f. Exponent
int_int_exp = int_num_1 ** int_num_2
int_float_exp = int_num_1 ** float_num_1
int_cmplx_exp = int_num_1 ** complex_num_1
float_float_exp = float_num_1 ** float_num_2
float_cmplx_exp = float_num_1 ** complex_num_1
cmplx_cmplx_exp = complex_num_1 ** complex_num_2

print(f'int_int_exp\ttype: {type(int_int_exp)}\tvalue: {int_int_exp}',
    f'\nint_float_exp\ttype: {type(int_float_exp)}\tvalue: {int_float_exp}',
    f'\nint_cmplx_exp\ttype: {type(int_cmplx_exp)}\tvalue: {int_cmplx_exp}',
    f'\nfloat_float_exp\ttype: {type(float_float_exp)}\tvalue: {float_float_exp}',
    f'\nfloat_cmplx_exp\ttype: {type(float_cmplx_exp)}\tvalue: {float_cmplx_exp}',
    f'\ncmplx_cmplx_exp\ttype: {type(cmplx_cmplx_exp)}\tvalue: {cmplx_cmplx_exp}',
    '\n')


# 3. Type conversion using built in functions

a, b, c, d, e = 25, 4.15, '3', '1.09', 1+2j

print(f'a = {a} {type(a)}, b = {b} {type(b)}, c = {c} {type(c)}, d = {d} {type(d)}, e = {e} {type(e)}\n')

print(f'a\ttype: {type(float(a))}\tvalue: {float(a)}'
    f'\nd\ttype: {type(complex(a))}\tvalue: {complex(a)}'
    f'\nb\ttype: {type(int(b))}\tvalue: {int(b)}'
    f'\nd\ttype: {type(complex(b))}\tvalue: {complex(b)}'
    f'\nc\ttype: {type(int(c))}\tvalue: {int(c)}'
    f'\nc\ttype: {type(float(c))}\tvalue: {float(c)}'
    f'\nc\ttype: {type(complex(c))}\tvalue: {complex(c)}'
    # f'\nd\ttype: {type(int(d))}\tvalue: {int(d)}'     # Raises ValueError
    f'\nd\ttype: {type(float(d))}\tvalue: {float(d)}'
    f'\nd\ttype: {type(complex(d))}\tvalue: {complex(d)}'
    # f'\ne\ttype: {type(int(e))}\tvalue: {int(e)}'     # Raises TypeError
    '\n')


# 4. Problem with decimal calculation in python3

x, y = 1.1, 2.2
z = x + y
print(f'x = {x}\ty = {y}\texpected z = 3.3\nz = {z}')     # A math error is noticeable
x, y = 1.2, 1
z =  x - y
print(f'x = {x}\ty = {y}\texpected z = 0.2\nz = {z}\n')     # A math error is noticeable

'''
Explanation to the anomaly:
It’s a problem caused when the internal representation of floating-point numbers, which uses a fixed number of binary digits to represent a decimal number. It is difficult to represent some decimal numbers in binary, so in many cases, it leads to small roundoff errors. 

In this case, taking 1.2 as an example, the representation of 0.2 in binary is 0.00110011001100110011001100…… and so on. It is difficult to store this infinite decimal number internally. Normally a float object’s value is stored in binary floating-point with a fixed precision (typically 53 bits). So we represent 1.2 internally in binary as,

1.0011001100110011001100110011001100110011001100110011  
Which is exactly equal to in decimal as :

1.1999999999999999555910790149937383830547332763671875
'''

# For such cases, decimal module comes to rescue
from decimal import Decimal

x = Decimal('1.1')
y = Decimal('2.2')
z = x + y
print(f'x = {x}\ty = {y}\texpected z = 3.3\nz = {z}')

x = Decimal('1.2')
y = Decimal('1')
z = x - y
print(f'x = {x}\ty = {y}\texpected z = 0.2\nz = {z}')
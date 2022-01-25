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
complex_num_3 = -1-2j
complex_num_4 = 1-2j
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


# The Python interpreter has a number of functions and types built into it that 
# are always available.

# They are listed here in alphabetical order.

# 1. abs()
'''
This function returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.
syntax:
abs(num)
where num can be integer, float and complex number
'''
# Example 1:
num1 = -20
num2 = -33.33
c_num = 5+4j
print(f'absolute value of {num1} is {abs(num1)}'
    f'\nabsolute value of {num2} is {abs(num2)}'
    f'\nmagnitude value of {c_num} is {abs(c_num)}'
    '\n')


# 2. any()
'''
This function returns True if any element of an iterable is True. If not, it returns False.
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
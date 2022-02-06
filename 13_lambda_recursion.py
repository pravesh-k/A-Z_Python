# Lambda Functions: Also known as Anonymous functions in python, are such 
#                   functions which do not have a name. The lambda can take any 
#                   number of arguments, but can only have one expression. While 
#                   normal functions are defined using the 'def' keyword in 
#                   Python, anonymous functions are defined using the 'lambda' 
#                   keyword. The lambda function does not requires a return 
#                   statement to return any resulting value.

'''
syntax:
lambda arguments: expression
'''

# Recursion: Recursion is a common mathematical and programming concept. 
#            In Python, we know that a function can call other functions. It is 
#            even possible for the function to call itself. These types of 
#            constructs are termed as recursive functions. Simply, it means that a 
#            function calls itself.

'''
**note 1: One should be very careful with recursion as it can be quite easy to 
slip into writing a function which never terminates, or one that uses excess 
amounts of memory or processor power. However, when written correctly recursion 
can be a very efficient and mathematically-elegant approach to programming.
'''


# # Contents:
#   1. Writing Lambda functions:
#   2. Lambda functions with other functions
#   3. Writing Recursive functions


# 1. Writing Lambda functions:

# Example 1: calculating gst amount
gst_amount = lambda cp: 0.18*cp
print(f'gst for amount 150 at 18% is: {gst_amount(150)}'
    f'\ngst for amount 2275 at 18% is: {gst_amount(2275)}'
    '\n')

# Example 2: calculating square of the input number
num_square = lambda num: num**2
print(f'square of 12: {num_square(12)}'
    f'\nsquare of 19: {num_square(19)}'
    '\n')



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


# 2. Lambda functions with other functions

# a. Using lambda func with in-built filter() function
# Example 1: filter the odd numbers from the list
a_list = [5, 9, 14 ,6, 36, 7, 8, 10, 11, 17, 109]
odd_list = list(filter(lambda i: i%2!=0, a_list))
print(f'odd_list: {odd_list}\n')

# Example 2: filter the number from a list if exists in another list
b_list = [5, 9, 14 ,6, 36, 7, 8, 10, 11, 17, 108]
special_list = list(range(3, 110, 3))
special_b_list = list(filter(lambda x: x in special_list, b_list))
print(f'special_b_list: {special_b_list}\n')

# b. Using lambda func with in-built map() function
# Example 1: creating a list of cubes from another list
c_list = list(range(0,10))
cubed_c_list = list(map(lambda i: i*i*i, c_list))
print(f'cubed_c_list: {cubed_c_list}\n')

# c. Using filter() and map() function together with lambda
# Example 1: creating list of squares from another list but only if the num is even
square_even_c_list = list(map(lambda i: i*i, filter(lambda i: i%2==0, c_list)))
print(f'square_even_c_list: {square_even_c_list}\n')


# 3. Writing Recursive functions

# Example 1: A recursive function to find the factorial of number
def fact_recur(num):
    return 1 if num == 1 else num * fact_recur(num - 1)

print(f'factorial of 5 is: {fact_recur(5)}'
    f'\nfactorial of 10 is: {fact_recur(10)}'
    '\n')

# Example 2: A recursive function to find n fibonacci numbers in sequence
def fibo_recur(n):
    if n <= 1:
        return n
    else:
        return fibo_recur(n-1) + fibo_recur(n-2)

print(f'fibonacci sequence with n=5 : {[fibo_recur(i) for i in range(5)]}'
    f'\nfibonacci sequence with n=10 : {[fibo_recur(i) for i in range(10)]}'
    '\n')
# Function in Python: is a block of related statements designed to perform a 
#                     computational, logical, or evaluative task.
#                       
#                     The idea is to put some commonly or repeatedly done tasks 
#                     together and make a function so that instead of writing the 
#                     same code again and again for different inputs, we can do 
#                     the function calls to reuse code contained in it over and 
#                     over again.


'''
syntax:
def function_name(parameters):
    """docstring"""
    statement(s)
    return expression
'''

# # Content:
#   1. Creating and Calling a function
#   2. Arguments of a function
#   3. Types of arguments
#   4. Docstring
#   5. return statement
#   6. Pass by Reference


# 1. Creating and Calling a function
'''def keyword can be used to create a function.'''

# a. Creating a function
# Example 1: simple python function
def func():
    print('Hello World!')

# b. Calling a function
# Example 1: calling the function create above
'''After creating a function it can be called using the name of the function 
followed by parenthesis (containing parameters of that particular function if any).
'''
func()

# Example 2: calling the function multiple times
func()
func()
func()

# printing the type of the created function
print(type(func), '\n')


# 2. Arguments of a function
'''Argument are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.'''

# Example 1: function with one argument
def even_odd(num): 
    print(f'{num} is even\n') if num % 2 == 0 else print(f'{num} is odd\n')

even_odd(10)
even_odd(17)

# Example 2: function with three arguments
def sum_of_3_num(num1, num3, num2):
    print(f'sum = {num1+num2+num3}\n')

sum_of_3_num(3, 4, 7)
# sum_of_3_num(1, 2)    #TypeError: 3 arguments expected but provoded only 2

'''
**note 1:
The terms parameter and argument can be used for the same thing: information that 
are passed into a function. 
From a function's perspective: A parameter is the variable listed inside the 
parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
'''

# 3. Types of arguments

# a. Default arguments: A default argument is a parameter that assumes a default 
#                       value if a value is not provided in the function call for 
#                       that argument.
# Example 1:
def my_func(x, y=50):
    print(f'x is {x}')
    print(f'y is {y}\n')

my_func(10)
my_func(10, 20)
my_func(y = 10, x = 20)

'''
** note 2: 
Any number of arguments in a function can have a default value. But once we have a default argument, all the arguments to its right must also have default values

for ex:
def func_2(a, b=10, c):     # SyntaxError: c can't not accessed
    statement(s)
'''

def my_func_2(a, b=16, c=25):
    print(f'a is {a}')
    print(f'b is {b}')
    print(f'c is {c}\n')

my_func_2(9)
my_func_2(9, 36)
my_func_2(9, 64, 81)
my_func_2(9, c=81)
my_func_2(c=81, a=100)


# 4. Docstring


# 5. return statement


# 6. Pass by Reference


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



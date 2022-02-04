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
#   7. Function within function


# 1. Creating and Calling a function
'''def keyword can be used to create a function.'''

# a. Creating a function
# Example 1: simple python function
from unittest import result


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
    print(f'x is {x} and y is {y}\n')

my_func(10)
my_func(10, 20)

'''
** note 2: 
Any number of arguments in a function can have a default value. But once we have a default argument, all the arguments to its right must also have default values

for ex:
def func_2(a, b=10, c):     # SyntaxError: c can't not accessed
    statement(s)
'''

# Example 2: 
def my_func_2(a, b=16, c=25):
    print(f'a is {a} and b is {b} and c is {c}\n')

my_func_2(9)
my_func_2(9, 36)
my_func_2(9, 64, 81)

# b. Keyword arguments: The idea is to allow the caller to specify the argument 
#                       name with values so that caller does not need to remember 
#                       the order of parameters. 
# Example 1:
def name_of_childs(child1, child2, child3):
    print(f'child1: {child1}, child2: {child2} and child3: {child3}\n')

name_of_childs(child1='Adam', child2='Bob', child3='Chan')
name_of_childs(child2='Adam', child3='Bob', child1='Chan')

# Example 2:
def name_of_parents(parent1, parent2, parent3='James'):
    print(f'parent1: {parent1}, parent2: {parent2} and parent3: {parent3}\n')

name_of_parents(parent2='Andrew', parent1='Freddy')
name_of_parents(parent2='Andrew', parent3='Olivia', parent1='Freddy')

# c. Variable arguments: In Python, variable number of arguments can be passed to
#                        a function using special symbols i.e. if the number of 
#                        arguments are not known that will be passed to the 
#                        function, we can use the special symbols(* and **).
#                        Thus, also known as, Arbitrary Arguments and Arbitrary 
#                        Keyword Arguments.

# i. Variable length non-keywords argument (denoted by *args):
# Example 1:
def list_of_students(*args):
    for arg in args:
        print(arg, end=" ")
    print('\n')

list_of_students('Brad', 'Rohan', 'Jack')
list_of_students('Brad', 'Rohan', 'Jack', 'Dan')

# Example 2:
def list_of_objects(*args):
    for arg in args:
        print(arg, end=" ")
    print('\n')

list_of_objects('Henry', 15, ['black', 'red'], True)
list_of_objects(2, 4, 6, 8)

# ii. Variable length keyword arguments (denoted by **kwargs):
def country_capital(**kwargs):
    for keyname, value in kwargs.items():
        print(f'keyname={keyname}: value={value}')
    print()

country_capital(india='delhi', england='london', france='paris')
country_capital(india='', england='london')

# iii. employing *args and **kwargs together
def employee(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for keyname, value in kwargs.items():
        print(f'key={keyname}: value={value}')
    print()
    
employee(101, '45D', 'Sales', first_name='Iaan', last_name='Jobs', salary=150000)


# 4. Docstring
'''
**note 3: The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function. The use of docstring in functions is optional but it is considered a good practice.

syntax:
def function_name(parameters):
    statement(s)
    return expression

And to print the docstring of a function call,
function_name.__doc__
'''

# Example 1:
def sum_of_nums(*args):
    """This function calculates the sum of variable number of inputs"""
    sum = 0
    for arg in args:
        sum += arg
    print(f'sum = {sum}\n')

print(sum_of_nums.__doc__, '\n')
sum_of_nums(1, 3, 2)
sum_of_nums(1, 3, 2, 4, 5)


# 5. return statement
'''
**note 3: The function's return statement is used to exit from a function and go 
back to the function caller and return the specified value or data item to the 
caller.

The return statement can consist of a variable, an expression, or a constant which 
is returned to the end of the function execution. If none of the above is present 
with the return statement a None object is returned.'''

# Example 1:
def prod_of_nums(*args):
    '''This function returns the product of input numerical values'''
    pro = 1
    for arg in args: pro *= arg
    return pro

print(prod_of_nums.__doc__,'\n')
result = prod_of_nums(2, 3, 4)
print(f'prod_result = {result}')
print(f'prod_result = {prod_of_nums(14, 9)}\n')

# Example 2:
def is_even(val):
    '''This function returns whether the input is even or not'''
    return True if val%2==0 else False

print(f'is 11 even: {is_even(11)}')
print(f'is 312100 even: {is_even(312100)}\n')


# 6. Pass by Object Reference
'''
**note 4: Pass by value: In pass-by-value, the function receives a copy of the  
    argument objects passed to it by the caller, stored in a new location in 
    memory. Values of parameter are passed to the function, if any kind of change 
    done to those parameters inside the function, those changes not reflected back 
    in your actual parameters.
    
    WHEREAS in,
    
    Pass by Reference: In pass-by-reference, the function receives reference to 
    the argument objects passed to it by the caller, both pointing to the same 
    memory location. The reference of parameters is passed to the function. If any 
    changes made to those parameters inside function those changes are get 
    reflected back to your actual parameters.
    
    BUT,
    
    In Python 'neither' of these two concepts are applicable, rather the values 
    are sent to functions by means of object reference.

    SO,

    Pass by object reference: In Python, (almost) everything is an object. 
    "Variables" in Python are more properly called "Names". Likewise, "assignment" 
    is really the binding of a name to an object. Each binding has a scope that 
    defines its visibility, usually the block in which the name originates.

    In Python,Values are passed to function by object reference.
    
    If object is immutable(not modifiable) than the modified value is not available outside the function.
    
    If object is mutable (modifiable) than modified value is available outside the function.
'''

# Example 1: List is a mutable object, when passed to func and performed any 
#            changes to it, it is reflected in the original object
def test_func(var):
    print(f'memory address of the var argument: {id(var)}')
    var[0] = 15

lst = [9, 2, 7, 8, 1]
print(f'memory address of lst object: {id(lst)}')
print(f'lst before passing to test_func: {lst}')
test_func(lst)
print(f'lst after passing to test_func: {lst}\n')

# in the above case it can be seen that the lst object and var argument has same 
# memory address

# Example 2: When list object passed to the function is completely assigned a new 
#            list value, then it's address changes and it is actually not 
#            reflected in the original object which was passed to the function as 
#            an argument.

def test_func_2(var):
    print(f'memory address of the var argument: {id(var)}')
    var = [10, 20, 30]
    print(f'memory address of the var after replaced with a new list: {id(var)}')

lst2 = [1, 2, 3, 4]
print(f'memory address of the lst2 object: {id(lst2)}')
print(f'lst2 before passing to test_func_2: {lst2}')
test_func_2(lst2)
print(f'lst2 after passing to test_func_2: {lst2}\n')

# in the above case it can be seen that the lst2 object and var argument has same 
# memory address but after the value of the var object is replaced with a new list 
# inside the function, the reference of var to the lst2 object is broken and a new 
# memory block is assigned to the var object inside the function. Thus value of 
# lst2 object remains unchanged.

# Example 3: When a immutable object is passed to a function, and it is modified, 
#            the reference to the original object pass is broken as well.

def test_func_3(var):
    print(f'memory address of the var argument: {id(var)}')
    var = 100
    print(f'memory address of the var after assigning a new numeric value: {id(var)}')

num = 50
print(f'memory address of the num object: {id(num)}')
print(f'num before passing to test_func_3: {num}')
test_func_3(num)
print(f'num after passing to test_func_3: {num}\n')

# Example 4: Swap function
def swap_1(x, y):
    print(f'x = {x} and y = {y}')
    x, y = y, x
    print(f'after swapping, x = {x} and y = {y}')

a, b = 10, 15
print(f'a = {a} and b = {b}')
swap_1(a, b)
print(f'after passing to swap_1 function, a = {a} and b = {b}\n')

# in the above example we can see that swap_1 function didn't do any changes to 
# the objects a, b even if the the x, y arguments seem to have swapped the values 
# with each other. This happened due to the fact that the reference to the 
# objects, a and b are broken as soon as the values of x and y are changed.

# Example 5: return statement can be used to perform the above desired operation 
#            of swap

def swap_2(x, y):
    # print(f'x = {x} and y = {y}')
    x, y = y, x
    # print(f'after swapping, x = {x} and y = {y}')
    return x, y

a, b = 10, 15
print(f'a = {a} and b = {b}')
a, b = swap_2(a, b)
print(f'after passing to swap_2 function, a = {a} and b = {b}\n')

# in the above example, the values of a and b are swapped successfully using the 
# return statement to return the changes in x and y arguments, and then the return 
# value of swap_2 function is assigned to the objects a and b, thus changing the 
# original values of a and b as well there memory address are changed to the 
# address of the variables x and y which are returned and assigned to original 
# objects a and b.


# 7. Function within function
'''
**note 5: A function that is defined inside another function is known as the 
'inner function' or 'nested function'. Nested functions are able to access 
variables of the enclosing scope. These functions are used so that they can be 
protected from everything happening outside the function.
'''

# Example 1:
def func_top():
    msg = 'Welcome to the world of nesting'

    def nest_func_1():
        print(f'msg: {msg}\n')

    nest_func_1()

func_top()

# Example 2:
def add_100(var):
    var += 100

    def add_50(var):
        var += 50
        return var
    
    return add_50(var)

num = 30
print(f'passing num to add_100 func returns: {add_100(num)}\n')
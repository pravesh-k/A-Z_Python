## Python3
# Beginning of Python3

# Contents:
#   1. Commenting
#   2. Indentation
#   3. The in-built print function

# 1 Commenting
# Single line comments in python is identified-
# by a hash at the beginning of the comment.

'''Multi line comments in python is identified
when triple quotes are present at the start 
and end of the comment. Either single 
quote or double quotes can be 
used to serve the purpose
of multi-line comment'''

# 2 Indentation:
# Python uses indentation to highlight the blocks of code. Whitespace is used 
# for indentation in Python. All statements with the same distance to the right 
# belong to the same block of code. If a block has to be more deeply nested, it 
# is simply indented further to the right. You can understand it better by 
# looking at the following lines of code.

# Commented Python program showing indentation
   
# site = 'gfg'

# if site == 'gfg': 
#     print('Logging on to geeksforgeeks...') 
# else: 
#     print('retype the URL.') 
# print('All set !')

# 3 The in-built print function
# Basic use case of inbuilt print function,
# this displays output on the console.

print('First Hello World')
print("Second Hello World")
print('\n\n')

# print(A)    #This produces error
print('A', 'B', 'z')

print(10)
print(1, '\t', 2, '\t\t', 3)
print('')
print(5.55)
print(100, 5.55, 'Third Hello World')
print('\n')
print(10, 20, 30, sep='#')
print(10, 20, 30, end='#')
print()
print(True)
print(False)

#complex number
print(3+4j)     

# print('Hello ' + 5 + ' World')     #This produces error
print('A'+'b'+'X')
print('Hello ' + '5' + ' World')

# str() is a global built-in function that converts an object into its string representation.
print('Hello ' + str(6) + ' World')

print('A '*5)

# print(any_Object)

# Some more use cases of print function with variables and different datatypes can be seen in further programs.
# Decision making statements: are those statements that are used to make some 
#                             decisions and based on those decisions execution 
#                             of next block of code is done

# In Python, 'if' 'else' 'elif' statements are used for decision making. These 
# statements control the flow of the logic and code.

'''
**note 1: Decision making statements require logical expressions to valuate, these 
 expressions can be formed using comparison, logical, identity and membership 
 operators. Refer to '3_operators' module for operators.
'''


# # Contents:
#   1. if statement
#   2. else statement
#   3. elif statement


'''
**note 2: Python relies on indentation (whitespace at the beginning of a line) to 
 define scope in the code. Other programming languages often use curly-brackets 
 for this purpose.
 And so, if, else, elif statements, without indentation (will raise error)
'''


# 1. 'if' statement: 
'''
**note 3: if statement is the most simple decision-making statement. It is used to
 decide whether a certain statement or block of statements will be executed or not 
 i.e if a certain condition is true then a block of statement is executed 
 otherwise not.
'''

# Example 1:
from copy import copy


if 5 > 4:
    print('5 is greater than 4\n')

# Example 2: multiple if statements and block outside if statements
if 30 > 20:
    print('30 is greater than 20\n')
if 10 > 20:
    print('10 is greater than 20')
print('block outside the scope of if statement\n')

# Example 3:
val1 = 15
val2 = 18
if val1 <= val2:
    print(f'val1 : {val1} is less than or equal to val2 : {val2}\n')

# Example 4: Also called short hand if statement, helpful while executing single 
# line statements inside if block
if 'Hello' < 'World': print('Hello\n')

# Example 5: multi line code inside if block
if 'a' < 'b':
    print('line.. 1')
    print('line.. 2')
    print('line.. 3\n')

# Example 6: Nested if statements
if 'd' > 'c':
    if 5 > 2:
        print('Hello')
        if 3 > 4:
            print('Earth')
        if 10 > 4:
            print('World')
    print('Bye!\n')

# Example 7: condensing code in above example using logical operators along with 
#            conditional operators and short-hand if statemente

if 'd' > 'c' and 5 > 2:
    print('Hello')
    if 3 > 4: print('Earth')
    if 10 > 4: print('World')
    print('Bye!\n')

# Example 8: using identity operator in generating conditions for if statement
x = 10
y = x
if y is x:
    print('y is x\n')

# Example 9: using membership operator in generating conditions for if statement
x = [1, 2, 3, 5, 9]
if 9 in x:
    print('Present Sir!\n')

# Example 10: Use of if statement in list comprehension
squares = [x*x for x in [-5, 3, 8, -9, 2, 7, 0] if x >= 0]
print(f'squares : {squares}\n')


# 2. 'else' statement: 
'''
**note 4: Else is used with if statement to execute a block of code when the condition is false. 
'''

# Example 1:
if 5 < 4:
    print('\nLorem\n')
else:
    print('\nIpsum\n')

# Example 2: multiple if-else statements and block outside if-else statements
if 30 > 20:
    print('Apple')
else:
    print('Banana')
if 10 > 20:
    print('Cherry')
else:
    print('Dragon-fruit')
print('Onion is not fruit\n')

# Example 3:
val1 = 15
val2 = 15
if val1 < val2:
    print('Easy\n')
else:
    print('Difficult\n')

# Example 4: Also called short hand if statement, helpful while executing single 
# line statements inside if block
print('Sun\n') if 'Sun' < 'Moon' else print('Moon\n')

# Example 5: multi line code inside if-else block
if 'a' > 'b':
    print('line.. 1')
    print('line.. 2')
    print('line.. 3\n')
else:
    print('line.. a')
    print('line.. z\n')

# Example 6: Nested if-else statements
if 'd' < 'c':
    print('Stage..1')
else:
    if 100 == 200:
        print('Stage..2')
    else:
        if False == False:
            print('Stage..3')
        else:
            print('Stage..4')

# Example 7: condensing code in above example using short-hand if statemente

print('Stage..1') if 'd' < 'c' else print('Stage..2') if 100 == 200 else print('Stage..3') if False == False else print('Stage..4')

# Example 8: using identity operator in generating conditions for if-else statement
x = 10
y = -x
if y is x:
    print('y is x\n')
else:
    print('y is not x\n')

# Example 9: using membership operator in generating conditions for if statement
x = [1, 2, 3, 5, 9]
if 10 in x:
    print('10 Present Sir!\n')
else:
    if 'h' in 'hello':
        print('h Present Sir!\n')
    else:
        print('10 and hello not present\n')

# Example 10: Use of if-else statement in list comprehension
raised = [x*x if x <= 0 else x**3 for x in [-5, 3, 8, -9, 2, 7, 0]]
print(f'raised : {raised}\n')


# 3. 'elif' statement: 
'''
**note 5: Elif is a condensed way to write else-if statement, i.e. it clubs the two statements. 
'''

# Example 1:
if 5 < 4:
    print('\nLorem\n')
elif 1 > 0:
    print('\nIpsum\n')

# Example 2: multiple if-elif statements and block outside if-elif statements
if 30 > 20:
    print('Apple')
elif 'z' > 'a':
    print('Banana')
if 10 > 20:
    print('Cherry')
elif 'u' > 'e':
    print('Dragon-fruit')
print('Onion is not fruit\n')

# Example 3: elif with else
val1 = 15
val2 = 15
if val1 < val2:
    print('Easy\n')
elif val1 > val2:
    print('Difficult\n')
else:
    print('Tough\n')

# Example 4: multi line code inside if-else block
if 'a' > 'b':
    print('line.. 1')
    print('line.. 2')
    print('line.. 3\n')
elif 2*2 > 1*1:
    print('line.. a')
    print('line.. z\n')

# Example 5: Nested if-else statements
if 'd' < 'c':
    print('Stage..1')
elif 100 == 200:
    print('Stage..2')
elif False == False:
    print('Stage..3')
else:
    print('Stage..4')

# Example 6: using identity operator in generating conditions for if-else statement
x = 10
y = -x
if y is x:
    print('y is x\n')
elif y == -10:
    print('y is not x and y is = -10\n')
else:
    print('y is unknown\n')

# Example 7: using membership operator in generating conditions for if statement
x = [1, 2, 3, 5, 9]
if 10 in x:
    print('10 Present Sir!\n')
elif 'h' in 'hello':
    print('h Present Sir!\n')
else:
    print('10 and hello not present\n')

# Example 8: using logical operators with elif
x = 'F'
if x >= 'a' and x <= 'z':
    print('x is in lower case\n')
elif x >= 'A' and x <= 'Z':
    print('x is in upper case\n')
else:
    print('x is unknown')

# Example 9: pass statement
'''
**note 6: if statements cannot be empty, but if for some reason an there is an if
 statement with no content, put in the pass statement to avoid getting an error.

pass does nothing, it is simply a null statement. The interpreter does not ignore
 a pass statement, but nothing happens and the statement results into no
 operation. The pass statement is useful when implementation of a function is not
 yet ready but it will be implemented in the future.
 '''

# no output generated with the below code
if 'a' < 'b':
    pass
elif 1 > 0:
    pass
else:
    pass
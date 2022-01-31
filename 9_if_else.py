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


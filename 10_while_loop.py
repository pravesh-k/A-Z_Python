# While Loop: It is used to execute a block of statements repeatedly until a
#             given condition is satisfied. And when the condition becomes false, 
#             the line immediately after the loop in the program is executed. 
#             While loop falls under the category of indefinite iteration. 

#             Indefinite iteration means that the number of times the loop is   
#             executed isn’t specified explicitly in advance. 

'''
syntax:
while expression:
    statement(S)
'''


# # Content:
#   1. While loop
#   2. Single statement while block
#   3. Loop Control Statements
#   4. While loop with else
#   5. Sentinel control statement
#   6. While loop on different data structures


# 1. While loop

# Example 1: printing Hello World three times
count = 0
while count < 3:        # iterate this block till value of count is less than 3
    count = count + 1       # increment the value of count by 1
    print(f'Hello World {count}')
print()     #this line is out of while block


# 2. Single statement while block

# Example 1: multi-statement inside single statement while loop
count = 3
while count < 6: count = count + 1; print(f'Hello Python {count}')
print()

# Example 2: nested compound statements inside single statement while loop
steps = 0
while steps < 6: print(f'Bonjour! {steps}') if steps % 2 == 0 else print(f'Adios {steps}'); steps += 1
'''note that short-hand if-else statement is used'''
print()


# 3. Loop Control Statements

# a. continue statement: continue statement returns the control to the beginning 
# of the loop.
# Example 1
count = 0
while count < 3:
    count += 1
    print('Indian')
    continue
    print('Non-Indian')     # this line is never executed due to conitnue statement
print()

# Example 2: print all letters except 'l' and 'o'
welcome = 'HelloFolks,WelcomeToTheWhileLoop'
index = 0

while index < len(welcome):
	if welcome[index] == 'l' or welcome[index] == 'o':
		index += 1
		continue
		
	print(welcome[index], end=" ")
	index += 1
print()

# b. break statement: break statement brings control out of the loop.
# Example 1:
count = 0
while count < 3:
    count += 1
    print('\nAmerican')
    break
    print('Non-American')     # this line is never executed due to break statement
print()

# Example 2: break the loop as soon as 'o' is found
welcome = 'HelloFolks,WelcomeToTheWhileLoop'
index = 0

while index < len(welcome):
	if welcome[index] == 'o':
		index += 1
		break
		
	print(welcome[index], end=" ")
	index += 1
print()


# 4. While loop with else


# 5. Sentinel control statement


# 6. While loop on different data structures
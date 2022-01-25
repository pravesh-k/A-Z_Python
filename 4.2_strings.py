# In Python, Strings are arrays of bytes representing Unicode 
# characters. However, Python does not have a character data 
# type, a single character is simply a string with a length of 1


# Contents:
#   1. Strings creation
#   2. Accessing characters of strings
#   3. String Slicing
#   4. Deleting/Updating in strings
#   5. Escape Sequencing
#   6. Formatting of Strings
#   7. String methods


# 1. Strings creation

# Strings can be defined with single quotes, double quotes and triple 
# quotes as well
string1 = 'Hello world with single quotes'
string2 = "Hello world with double quotes"
string3 = '''Hello world with triple quotes'''
string4 = '''Hello world
with a structual format
Left    
        Center      
                Right
End of line'''

print(f'string1: {string1}\nstring2: {string2}\nstring3: {string3}\nstring4: \n{string4}\n')


# 2. Accessing characters of strings

'''
 **note 1: Individual characters of a String can be accessed by using the
  method of Indexing. Indexing also allows negative address references to 
  access characters from the back of the String, e.g. -1 refers to the 
  last character, -2 refers to the second last character, and so on.
  Indexing in positive starts from 0. And the characters of a string
  can be accessed using square brackets '[]'
'''

print(f'first character of string1 is: {string1[0]}'
    f'\nlast character of string1 is: {string1[-1]}'
    f'\nninth character of string1 is: {string1[8]}'
    '\n')



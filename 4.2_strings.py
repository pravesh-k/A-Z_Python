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


# 3. String Slicing

# To access a range of characters in the String, the method of slicing is 
# used. Slicing in a String is done by using a Slicing operator (colon).
# Strings can't be accessed from backwards/reverse.

print(f'slicing characters of string1 from 3-12: {string1[3:12]}'
    f'\nslicing characters of string1 between 3rd and 2nd last character: {string1[3:-2]}'
    f'\nslicing characters of string1 between 15th last and 2nd last character: {string1[-15:-2]}'
    f'\nslicing characters of string1 after 10th character: {string1[10:]}'
    f'\nslicing characters of string1 upto 10th character: {string1[:10]}'
    '\n')


# 4. Deleting/Updating in strings

'''
**note 2: Updation or deletion of characters from a String is not allowed. 
This will cause an error because item assignment or item deletion from a 
String is not supported. Although deletion of the entire String is 
possible with the use of a built-in 'del' keyword. This is because Strings 
are immutable, hence elements of a String cannot be changed once it has 
been assigned. Only new strings can be reassigned to the same name. 
'''

statement = 'This is an old statement'
print(f'statement: {statement}\n')
# statement[2] = 'p'    # Raises TypeError
statement = 'This is an updated statement'
print(f'statement: {statement}\n')

# del statement[3]      # Raises TypeError
del statement
# print(f'statement: {statement}\n')    # Raises NameError


# 5. Escape Sequencing

'''
**note 3: Printing Strings with single and double quotes in it causes
 SyntaxError because strings are defined using single/double quotes.
 Hence, to print such a string either triple quotes are used or escape 
 sequences are used to print such strings.

 Escape sequences start with a backslash and can be interpreted 
 differently. If single quotes are used to represent a string, then all 
 the single quotes present in the string must be escaped and same is done 
 for Double Quotes. 

 To ignore the escape sequences in a String, 'r' or 'R' is used, this implies that the string is a raw string and escape sequences inside it are to be ignored.
'''

string5 = "Hello 'World"
string6 = 'Hel"lo \'World'
string7 = '''Hello 'Wor"ld'''
string8 = "Hell\"o 'World"

print(f'Escaping single quote using double quotes for string creation, string5: {string5}'
    f'\nEscaping single and double quote using escape sequence for single quote, string6: {string6}'
    f'\nEscaping single and double quote using triple quotes for string creation, string7: {string7}'
    f'\nEscaping single and double quote using escape sequence for double quote, string8: {string8}'
    '\n')

string9 = 'This is \x45\x47\x47\x53 in \x48\x45\x58'
print(f'escaping HEX format\n{string9}')
string10 = r"This is \x45\x47\x47\x53 in \x48\x45\x58"
print(f'ignoring HEX format\n{string10}')


# 6. Formatting of Strings




# 7. String methods
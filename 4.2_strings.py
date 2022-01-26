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

 To ignore the escape sequences in a String, 'r' or 'R' is used, this 
 implies that the string is a raw string and escape sequences inside
 it are to be ignored.
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
print(f'ignoring HEX format\n{string10}\n')


# 6. Formatting of Strings

'''
**note 4: Strings in Python can be formatted with the use of format() method 
which is a very versatile and powerful tool for formatting Strings. 
Format method in String contains curly braces {} as placeholders 
which can hold arguments according to position or keyword to 
specify the order.
'''

# Default Order
string11 = "{} {} {}".format('Good', 'Luck', 'Developer')
# Positional Formatting
string12 = "{2} {0} {1}".format('Good', 'Luck', 'Developer')
# Keyword Formatting
string13 = "{d} {u} {z}".format(z='Good', d='Luck', u='Developer')
print(f'default formatting on string11: {string11}'
    f'\npositional formatting on string12: {string12}'
    f'\nkeyword formatting on string13: {string13}'
    '\n')

# Integer and float formatting & rounding float decimals

# Formatting of Integers
string14 = "{0:b}".format(16)
string17 = "{0:x}".format(16)
# Formatting of Floats
string15 = "{0:e}".format(165.6458)
# Rounding off Integers
string16 = "{0:.2f}".format(1/6)
print(f"Binary representation of 16 is {string14}",
    f"\nHex representation of 16 is {string17}",
    f"\nExponent representation of 165.6458 is {string15}",
    f"\nTwo decimal rounding of 1/6 is : {string16}",
    '\n')

# A string can be left() or center(^) justified with the use of 
# format specifiers, separated by a colon(:).

# String alignment
string18 = "|{:<10}|{:^10}|{:>10}|".format('Coding', 'for', 'Life')
print(f"\nleft, center and right alignment with Formatting:\n{string18}")
 
# To demonstrate aligning of spaces
string19 = "\n!{0:^19} was founded in {1:<8}!".format("CodingForLife", 2005)
print(f"\naligning of spaces with Formatting:\n{string19}\n")


# 7. String methods

'''
capitalize()	Converts the first character of the string to a uppercase
casefold()	    Implements caseless string matching
center()	    Pad the string on left and right with the specified character.
count()	        Returns the number of occurrences of a substring in the string.
encode()	    Encodes strings with the specified encoded scheme
endswith()	    Returns “True” if a string ends with the given suffix
find()	        Returns the lowest index of the substring if it is found
format()	    Formats the string for printing it to console
format_map()	Formats specified values in a string using a dictionary
index()	        Returns the position of the first occurrence of a substring
isalnum()	    Checks whether all characters are alphanumeric or not
isalpha()	    Checks whether all characters in the string are alphabets
isdecimal()	    Checks whether all characters in a string are decimal
isdigit()	    Checks whether all characters in the string are digits
isidentifier()	Check whether a string is a valid identifier or not
islower()	    Checks if all characters in the string are lowercase
isnumeric()	    Checks whether all characters are numeric characters
isspace()	    Checks whether all characters are whitespace characters
istitle()	    Returns “True” if the string is a title cased string
isupper()	    Checks if all characters in the string are uppercase
join()	        Returns a concatenated string
ljust()	        Left aligns the string according to the width specified
lower()	        Converts all uppercase characters in a string into lowercase
lstrip()	    Returns the string with leading characters removed
partition()	    Splits the string at the first occurrence of the separator 
replace()	    Replaces all occurrences of a substring with another substring
rfind()	        Returns the highest index of the substring
rindex()	    Returns the highest index of the substring inside the string
rjust()	        Right aligns the string according to the width specified
rpartition()	Split the given string into three parts
rsplit()	    Split the string from the right by the specified separator
rstrip()	    Removes trailing characters
splitlines()	Split the lines at line boundaries
startswith()	Checks whether if a string starts with the given prefix
strip()	        Returns the string with both leading and trailing characters
swapcase()	    Converts all uppercase characters to lowercase and vice versa
title()	        Convert string to title case
translate()	    Modify string according to given translation mappings
upper()	        Converts all lowercase characters in a string into uppercase
'''
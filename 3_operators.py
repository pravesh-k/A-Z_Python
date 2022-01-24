# # Contents:
#   1. Arithmetic Operators
#   2. Assignment operators
#   3. Comparison operators
#   4. Logical operators
#   5 .Identity operators
#   6. Membership operators
#   7. Bitwise operators

# 1. Arithmetic Operators: used with numeric values to perform common 
# mathematical operations

a = 10
b = 5
# Addition
print('a + b =',a + b)
# Subtraction
print('a - b =', a - b)
# Multiplication
print('a * b =', a * b)
# Division
print('a / b =', a / b)
# Modulus
print('a "%" b =', a % b)
# Exponentiation
print('a ** b =', a ** b)
# Floor division
print('a // b =', a // b,'\n')


# 2. Assingment Operators: used to assign values to variables

c = 5
print('c =', c)
c += 3
print('c += 3, c =', c)
c = 5
c -= 3
print('c -= 3, c =', c)
c = 5
c *= 3
print('c *= 3, c =', c)
c = 5
c //= 3
print('c //= 3, c =', c)
c = 5
c /= 3
print('c /= 3, c =', c)
c = 5
c %= 3
print('c %= 3, c =', c)
c = 5
c **= 3
print('c **= 3, c =', c)
c = 5
c &= 3
print('c &= 3, c =', c)
c = 5
c |= 3
print('c |= 3, c =', c)
c = 5
c ^= 3
print('c ^= 3, c =', c)
c = 40
c >>= 3
print('c >>= 3, c =', c)
c = 5
c <<= 3
print('c <<= 3, c =', c, '\n')


# 3. Comparision Operators: used to compare two values

# Equal
print('5 == 3 returns', 5 == 3)
print('4 == 4 returns', 4 == 4)

# Not Equal
print('5 != 3 returns', 5 != 3)
print('4 != 4 returns', 4 != 4)

# Greater than
print('5 > 3  returns', 5 > 3)
print('4 > 4  returns', 4 > 4)
print('3 > 4  returns', 3 > 4)

# Less than
print('5 < 3  returns', 5 < 3)
print('4 < 4  returns', 4 < 4)
print('3 < 4  returns', 3 < 4)

# Greater than or equal to
print('5 >= 3 returns', 5 >= 3)
print('4 >= 4 returns', 4 >= 4)
print('3 >= 4 returns', 3 >= 4)

# Less than or equal to
print('5 <= 3 returns', 5 <= 3)
print('4 <= 4 returns', 4 <= 4)
print('3 <= 4 returns', 3 <= 4, '\n')


# 4. Logical Operators: used to combine conditional statements

# 'and' operator
print('3 < 5 and 3 < 10 returns', 3 < 5 and 3 < 10)
print('8 < 5 and 8 < 10 returns', 8 < 5 and 8 < 10)

# 'or' operator
print('3 < 5 or 3 < 10 returns', 3 < 5 or 3 < 10)
print('8 < 5 or 8 < 10 returns', 8 < 5 or 8 < 10)

# 'not' operator
print('not(3 < 5 and 3 < 10) returns', not(3 < 5 and 3 < 10))
print('not(8 < 5 and 8 < 10) returns', not(8 < 5 and 8 < 10), '\n')

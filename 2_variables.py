# # Contents:
#   1. Commenting
#   2. The in-built print function

# Defining variables in Python3

a = 1
print(a)

b = 0
print(b)

c = True
print(c)

d = False
print(d)

e = 10
print(e)

f = 00
print(f)

# Produces error
# g = A     
# print(g)

h = 'A'
print(h)

# Produces error
# i = This is a string

i = 'This is a string'
print(i)
j = "This is also string"
print(j)
k = '100'
l = 100
print('k =', k, 'is of type string\n    but', 'l =', l, 'is of type int or numeric')
print(f'printing using f-string techinque\n    k = {k} and l = {l}')
print('printing using string formatting techinque\n    k = {} and l = {}'.format(k, l))

m = 50
n = m
print(f'm = {m}, n = {n},\n    here the value of n is assigned using m')

n = m = 50
print(f'm = {m}, n = {n},\n    here also the value of n is assigned using m\n    but the here the value is assigned to\n    m and n simultaneously')

## illegal ways to assign value
# m = 50 = n and 50 = m = n
# 3 = 4
# 3 = a
# a + b = 3

o, p, q = 10, 20, 'Bye'
print(f'o = {o}, p = {p}, q = {q}, simultaneous value assignment to\n   variables but values are different')

r = 'Ok' + q
print(r)

s = t = p + 15
print(f's = {s}, t = {t}, p = {p},\n    s and t are assigned the\n  final sum value of p and 15')

u = 15
u = u - 5
print(f'u = {u}')
# same can be achieved by compound assignment operator
u -= 5
print(f'u = {u}')

# more examples of compound assignment operators
v = 20
v += 3
print(f'v = {v}')

w = 30
w /= 10
print(f'w = {w}')

x = 4
x //= 3
print(f'x = {x}')

y = 8
y *= 4
print(f'y = {y}')

z = 100
z %= 7
print(f'z = {z}')

# These variables are "constants" by convention:
NUMBER_OF_DAYS_IN_A_WEEK = 7
print(f'number of days in a week = {NUMBER_OF_DAYS_IN_A_WEEK}')
NUMBER_OF_MONTHS_IN_A_YEAR = 12
print(f'number of months in a year = {NUMBER_OF_MONTHS_IN_A_YEAR}')

# Nothing is actually stopping us from redefining them...
NUMBER_OF_DAYS_IN_A_WEEK = 8
print(f'number of days in a week = {NUMBER_OF_DAYS_IN_A_WEEK}')
# ...but it's probably not a good idea.
PI = 3.14
print(f'value of mathematical constant pi = {PI}')

# we can use the assignment operator to assign new values to the variables
aa = 3
print(f'aa = {aa}')
aa = 2
print(f'aa = {aa}')

bb = "jane"
print(f'bb = {bb}')
bb = "bob"
print(f'bb = {bb}')
BB = 150
print(f'BB = {BB}, is different than bb as\n     python is case-sensitive')

# cc += 10 # Produces error as cc is not defined prior to sum operation

# dd = any_object
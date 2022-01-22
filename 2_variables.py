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
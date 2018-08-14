import re

s = 'A83C72D1D8E67'

r = re.match('\d', s)
print(r)
r1 = re.search('\d', s)
print(r1.span())

s1 = 'Life is short, I use Python'
r2 = re.search('Life(.*)Python', s1)
print(r2.group(1))
r3 = re.findall('Life(.*)Python', s1)
print(r3)
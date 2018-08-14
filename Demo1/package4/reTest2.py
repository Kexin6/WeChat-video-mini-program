import re

a = 'c|!~C++|0Java|1Pythonb|6JavaScript|C#'
b = 'python 111 java'
c = 'pytho0python1pythonn2pythonpython3'

print(re.findall('\d', a))

s = 'abc, acc, adc, aec, afc, ahc'
print(re.findall('a[cf]c', s))
print(re.findall('a[^cf]c', s))

print(re.findall('[a-z]{4,6}', b))
print(re.findall('[a-z]{4,6}?', b))

print(re.findall('python*', c))
print(re.findall('python+', c))
print(re.findall('python?', c))

d = 'PythonPythonPythonPythonJS'
print(re.findall('(Python){4}(JS)', d))

language  = 'PythonC#\n Java C'
print(re.findall('c#', language, re.I))
print(re.findall('c#.{1}', language, re.I | re.S))
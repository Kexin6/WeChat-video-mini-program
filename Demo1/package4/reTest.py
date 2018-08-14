import re

a = 'c|!~C++|0Java|1Pythonb|6JavaScript|C#'
result = re.findall("Python", a)

print(result)
if len(result) > 0:
    print("a has Python in it")
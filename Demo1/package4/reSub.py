import re
def convert(value):
    pass

language = 'PythonC#JavaC#PHPC#'
r = re.sub('C#', 'GO', language, 1)

print(r)

r2 = re.sub('C#', convert, language)
print(r2)
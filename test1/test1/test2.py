import sys
f = open(r"filtered_words.txt", "r")
line = f.readline()

while line:
    if (line == 'Fuck') | (line == 'Sex') | (line == 'Shit'):
        print('Not passed')
    else:
        print(line, end='')
        print('Passed')
        print("\n")
    line = f.readline()
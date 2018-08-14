from typing import List

__all__: List[str] = ['testc7']

testc8 = 'work'
testc7 = 'great'

# while loop
print('Example of while loop')
a = 0
while a < 10:
    print(a)
    a += 1
else:
    print('EOF')
#相当于不用else直接print EOF

# for loop
print('\nExample of for loop')
list = ['apple', 'orange', 'banana', 'grape']
for fruit in list:
    print(fruit.title())

#2D
list2 = [['apple', 'orange', 'banana', 'grape'],(1,2,3)]
for both in list2:
    for individual in both:
        print(individual, end = ' ')


#loop homework:
print('\n\n')
list3 = [1,2,3,4,5,6,7,8]
for x in range(1,8,2):
    print(x)

print('\n')
for x in range(0, len(list3), 2):
    print(list3[x], end=' ')

print('\n')
b = list3[0: len(list3): 2]
print(b)
a = input()
b = type(a)
print(b)
#或者在这里写 a = int(a)
if a == '1':
    print('apple')
elif a == '2':
    print('orange')
elif a == '3':
    print('banana')
else:
    print('shopping')


a = 1
b = 0
print(a or b)
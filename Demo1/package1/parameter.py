def test(name , age, school = 'UT'):
    print("My name is: " + name)
    print("My age is: " + str(age))
    print("My school is: " + school)


test(name = 'Kexin',  school = 'UT', age = 18)
test('kexin', '18', 'UT')

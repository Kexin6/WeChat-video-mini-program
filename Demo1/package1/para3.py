a = 1
def func1():
    a = 2
    def func2():
        a = 3
        print(a)
    func2()
func1()

b = 1
def func3():
    b = 2
    def func4():
        print(b)
    func4()
func3()

c = 1
def func5():
    def func6():
        c = 3
        print(c)
    func6()
func5()


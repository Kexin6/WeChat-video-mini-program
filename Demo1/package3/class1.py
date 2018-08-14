class Student():
    sum = 0 #和类相关的变量

   # name = 'Someone'
    #  age = 0


    #Constructor
    def __init__(self, name, age):
        print('test Constructor')
        self.name = name
        self.age = age
        print('Constructor: ' + str(age))
        print(name)



    def doHomework(self):
        self.sum += 1
        print('Homework')
        print("Method中的sum：" + str(self.sum))
        print('self.name: ' + self.name)

    def trial(self):
        Student.sum += 1
        self.__class__.sum += 1
        self.sum += 1 #没用


#行为要找对主体
class Printer():
    '''
    def printFile(self):
        print('name: ' + self.name)
        print('age: ' + str(self.age))
    '''
class Student(object):
    sum = 0 #和类相关的变量

   # name = 'Someone'
    #  age = 0


    #Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 0
       # self.__class__.sum += 1
       # print("当前学生总数： " + str(self.__class__.sum))



    def doHomework(self):
        self.sum += 1
        print('Homework')
        print("Method中的sum：" + str(self.sum))
        print('self.name: ' + self.name)

    def trial(self):
        Student.sum += 1
        self.__class__.sum += 1
        self.sum += 1 #没用

    @classmethod
    def plusSum(cls):
        cls.sum += 1
        print(cls.sum)
        #print(self.name)

    @staticmethod
    def add(x,y):
        print('This is static method')
        print(Student.sum)
       # print(self.name)


    def __marking(self, score):
        self.score = score
        print("This student's score is: " + str(self.score))

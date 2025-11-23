class MySuperClass1:
    def __init__(self, arg1):
        self.arg1 = arg1
        print('superclass1', self.arg1)

    def method1(self):
        print('method 1')

class MySuperClass2:
    def __init__(self, arg1):
        self.arg1 = arg1
        print('superclass2', self.arg1)

    def method2(self):
        print('method 2')

class MySuperClass3:
    def __init__(self, arg1):
        self.arg1 = arg1
        print('superclass3', self.arg1)

    def method3(self):
        print('method 3')

class MyClass(MySuperClass1, MySuperClass2, MySuperClass3):
    def __init__(self, arg1, arg2, arg3):
        super().__init__(arg1)
        super().__init__(arg2)
        super().__init__(arg3)

    def method(self):
        print('child class')


class MyClass(MySuperClass1, MySuperClass2, MySuperClass3):
    def __init__(self, arg1, arg2, arg3):
        print('*************')
        super(MyClass, self).__init__(arg1)
        super().__init__(arg1)
        super(MySuperClass1, self).__init__(arg2)
        super(MySuperClass2, self).__init__(arg3)
        MySuperClass2.__init__(self, arg1)
        print('****************')
    
    def method(self):
        print('child class')

print(MyClass.__mro__)
z = MyClass(1, 2, 3)
z.method3()

print("=============================")


for x in MyClass.__mro__:
    print(type(x), x, sep=' | ') 


MyClass.__mro__[0](1, 2, 3)


class MySuperClass1:
    def __init__(self, arg1):
        self.arg1 = arg1
        print('superclass1', self.arg1)

    def method1(self):
        pass


# print(type(MySuperClass1(9)))
# print("=====")

class MySuperClass2:
    def __init__(self, arg1):
        self.arg1 = arg1
        print('superclass2', self.arg1)

    def method2(self):
        pass

class MySuperClass3:
    def __init__(self, arg1):
        self.arg1 = arg1
        print('superclass3', self.arg1)

    def method3(self):
        pass

class MyClass(MySuperClass1, MySuperClass2, MySuperClass3):
    def __init__(self, arg1, arg2, arg3):
        super().__init__(arg1)
        # super().__init__(arg2)
        # super().__init__(arg3)

    def method(self):
        pass



z = MyClass(1,2,3)

class A:
    def __init__(self):
        print("Init A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Init B")

class C(A):
    def __init__(self):
        super().__init__()
        print("Init C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("Init D")

d = D()
print(D.__mro__)


for x in D.__mro__:
    print(type(x), x, sep='|')
    
    

class MySuperClass1:
    def __init__(self, arg1):
        self.arg1 = arg1
        print('superclass1', self.arg1)

    def method1(self):
        pass

class MySuperClass2:
    def __init__(self, arg2, arg4):
        self.arg2 = arg2
        print('superclass2', self.arg2)

    def method2(self):
        pass

class MySuperClass3:
    def __init__(self, arg3):
        self.arg3 = arg3
        print('superclass3', self.arg3)

    def method3(self):
        pass

class MyClass(MySuperClass1, MySuperClass2, MySuperClass3):
    def __init__(self, arg1, arg2, arg3):
        super(MyClass, self).__init__(arg1)
        super(MySuperClass1, self).__init__(arg2, arg1)
        super(MySuperClass2, self).__init__(arg3)
        # super(MyClass.__mro__[1], self).__init__(arg3)
 

    def method(self):
        pass

print(MyClass.__mro__)
# z = MyClass(1, 2, 3)
MyClass.__mro__[0](1, 2, 3)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print("i ran")

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        self.fff = length
        print("i ran 2")
#     ...
# class Square(Rectangle):
#     def __init__(self,g,h):
#         ...

# sq = Square(8,3)
# print(sq.length)
        
square = Square(4)
square.area()
print("**", square.length, square.width)


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


cube = Cube(3)
print(cube.surface_area())
print(cube.volume())
print(type(Cube.__mro__))
print(cube.length, cube.width, cube.fff)


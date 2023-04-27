from classes import MyClass


class MyDerivedClass(MyClass):
    """an exammple derived class"""

    i = 54321
    def __init__(self):
        self.my_var_a = 1
        self.my_var_b = 2

x = MyDerivedClass()

print('x.i: {}'.format(x.i))
print('x.f: {}'.format(x.f()))
print('x.my_var_a: {}'.format(x.my_var_a))
print('x.my_var_b: {}'.format(x.my_var_b))
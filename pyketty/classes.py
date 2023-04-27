class MyClass:
    """An example class"""
    i = 12345
    my_var_a, my_var_b = 0, 0

    def __init__(self, my_var_a, my_var_b):
        """instantiates the class"""
        self.data = []
        self.my_var_a = my_var_a
        self.my_var_b = my_var_b

    def f(self):
        """returns hello world, by passing to the private function"""
        return self.__private_f()
    
    def __private_f(self):
        """returns hello world, only accessible as a private functiuon"""
        return 'hello world'
    


    


x = MyClass(1, 2)

print('x.i: {}'.format(x.i))
print('x.f: {}'.format(x.f()))
print('x.my_var_a: {}'.format(x.my_var_a))
print('x.my_var_b: {}'.format(x.my_var_b))






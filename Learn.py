def dec(func):
    def wrapper(self, *args, **kwargs):
        print(f'Method {func.__name__}')
        return func(self, *args, **kwargs)

    return wrapper


class MyClass:
    @dec
    def say_hello(self):
        print('hi from class')

obj = MyClass()
obj.say_hello()
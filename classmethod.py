class MyClass:
    name = 'Alex'
    age = 5
    @classmethod
    def say_info(cls):
        print('Info of MyClass')
        print(f'Name of class: {cls.__name__}')
        print(f'Value of name: {cls.name}')
        print(f'Value of age: {cls.age}')

MyClass.say_info()

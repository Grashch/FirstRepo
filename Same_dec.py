def dec1(fun):
    def wrapper():
        print('dec 1')
        return wrapper

def dec2(fun):
    def wrapper():
        print('dec 3')
        return wrapper

def dec3(fun):
    def wrapper():
        print('dec 3')
        return wrapper
@dec1
@dec3
@dec2
def say_hello_with_3dec():
    print('say hi')

say_hello_with_3dec()
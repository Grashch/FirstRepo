def dec1(fun):
    def wrapper():
        print('dec 1')
        fun()
    return wrapper

def dec2(fun):
    def wrapper():
        print('dec 2')
        fun()
    return wrapper

def dec3(fun):
    def wrapper():
        print('dec 3')
        fun()
    return wrapper
@dec1
@dec2
@dec3
def say_hello_with_3dec():
    print('say hi')

say_hello_with_3dec()
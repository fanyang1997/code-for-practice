def print_msg():
    msg = "I'm closure"

    def printer():
        print(msg)
    return printer

closure = print_msg()

closure()


import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        print('args = {}'.format(*args))
        return func(*args, **kwargs)

    return wrapper


@log
def test(p):
    print(test.__name__ + " param: " + p)


test("I'm a param")

class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()

# class Person(object):
#     def talk(self):
#         print('person is talking......')
#
# class Chinese(Person):
#     def walk(self):
#         print('is walking...')
#
# c = Chinese()
# c.talk()
# c.walk()
#

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'

    def talk(self):
        print('person is talking...')

class Chinese(Person):
    def __init__(self, name, age, language):
        Person.__init__(self, name, age)
        self.language = language
        print(self.name, self.age, self.weight, self.language)
    def talk(self):
        print('%s is speaking chinese' % self.name)
    def walk(self):
        print('is walking...')

class American(Person):
    pass

c = Chinese('bigberg', 22, 'Chinese')
c.talk()
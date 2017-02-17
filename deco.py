def deco1(func):
    print(func.__name__)
    return func


@deco1  # yeah = deco1(yeah)
def yeah():
    print('This is YEAH!')

yeah()


class DecClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print(self.func.__name__)
        return self.func(*args)


@DecClass  # yo = DecClass(yo)
def yo(text):
    print('yo ' + text)

yo('yooooo')

class Memorize:
    def __init__(self, func):
        self.func = func
        self.memo = {}

    def __call__(self, arg):
        if arg in self.memo:
            return self.memo[arg]
        else:
            self.memo[arg] = self.func(arg)
            return self.memo[arg]

import time


def elapse(func):
    def f(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        print('Elapsed time : ' + str(end-start))
        return res
    return f


@elapse
@Memorize
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(100))

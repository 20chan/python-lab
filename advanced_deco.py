i = 1


def until(cond):
    def outer_wrap(func):
        def inner_wrap():
            while cond():
                func()
        return inner_wrap
    return outer_wrap


@until(lambda: i < 10)
def plus_i():
    global i
    i += 1

plus_i()
print(i)

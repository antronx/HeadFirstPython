def my_func(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()

def my_func2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

def my_func3(*args, **kwargs):
    if args():
        for a in args:
            print(a, end=' ')
        print()
    if kwargs():
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()

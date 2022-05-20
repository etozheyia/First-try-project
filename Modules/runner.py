import pytasks


def runner(*args):
    if args:
        for func in args:
            if hasattr(pytasks, func) and callable(getattr(pytasks, func)):
                print(getattr(pytasks, func)())
    else:
        for atr in dir(pytasks):
            if callable(getattr(pytasks, atr)) and not atr.startswith('__'):
                print(getattr(pytasks, atr)())


if __name__ == '__main__':
    runner()

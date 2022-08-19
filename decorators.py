import sys


def retry(count, exceptions='*'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            tested = 0
            while tested < count:
                try:
                    func(*args, **kwargs)
                except:
                    if exceptions == '*':
                        tested += 1
                        continue
                    inf = sys.exc_info()
                    if inf[0] in exceptions:
                        tested += 1
                        continue
                    else:
                        raise
        return wrapper
    return decorator


def ignore(exceptions='*'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                if exceptions == '*':
                    return
                inf = sys.exc_info()
                if inf[0] in exceptions:
                    return
                else:
                    raise
        return wrapper
    return decorator


def once(func):
    func()

    def decorator(*args, **kwargs):
        func(*args, **kwargs)
    return decorator

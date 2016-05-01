'''
General utilities
'''


from myflaskapp import app


def try_catch_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Warning as w:
            pass
            app.logger.warning(str(w))
        except Exception as e:
            pass
            app.logger.error(str(e))
    return wrapper

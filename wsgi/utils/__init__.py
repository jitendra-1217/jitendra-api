

def try_catch_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Warning as w:
            pass
            # logger.warning(str(w))
        except Exception as e:
            pass
            # logger.error(str(e))
    return wrapper

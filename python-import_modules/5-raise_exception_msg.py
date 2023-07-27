def raise_exception_msg(message=""):
    try:
        raise_exception_msg("Python is cool")
    except NameError as ne:
        print(ne)

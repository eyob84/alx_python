def raise_exception_msg(message=""):
    try:
        raise TypeError(message)
    except TypeError as ne:
        print(ne)

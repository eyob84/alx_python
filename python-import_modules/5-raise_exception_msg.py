def raise_exception_msg(message=""):
    try:
        raise TypeError('C is fun')
    except TypeError as ne:
        print(ne)

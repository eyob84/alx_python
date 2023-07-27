def raise_exception_msg(message=""):
    try:
        raise TypeError('C is fun')
    except NameError as ne:
        print(ne)

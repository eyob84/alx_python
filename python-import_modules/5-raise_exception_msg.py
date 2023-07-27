def raise_exception_msg(message=""):
    try:
        raise TypeError('Python is cool')
    except NameError as ne:
        print(ne)

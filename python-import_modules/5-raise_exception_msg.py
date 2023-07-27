def raise_exception_msg(message=""):
    try:
        raise NameError('C is fun')
    except NameError as ne:
        print("python is cool")

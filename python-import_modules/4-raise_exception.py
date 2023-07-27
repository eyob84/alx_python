def raise_exception():
    try:
        raise TypeError('HiThere')
    except TypeError as te:
        print(te)

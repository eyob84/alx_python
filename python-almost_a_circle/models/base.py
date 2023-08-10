class Base():
    __nb_objects = 0
    def __init__(self, id=None):
            """this is a base class """
            if id:
                  self.id = id
            else:
                 __nb_objects +=1  
                 self.id=__nb_objects
    __doc__ = """
    this is documentation for my class
    """
    

__doc__ = """
this is documentation for my module
"""

            
class base():
    __nb_objects = 0
    def __init__(self, id=None):
            """this is a base class """
            if id!=None:
                  self.id = id
            else:
                 __nb_objects +=1  
                 self.id=__nb_objects
    __doc = """
    this is documentation for my class
    """
    

doc = """
this is documentation for my module
"""

            
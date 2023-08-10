from models.base import Base
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """sadfafa """
        super().__init__(id)
        self.__width=width
        self.__height=height
        self.__y=y
        self.__x=x
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        self.__width= value

    __doc__ = """
    this is documentation for my class
    """
    

__doc__ = """
this is documentation for my module
"""

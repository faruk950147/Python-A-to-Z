def newFind(cls, *args, **kwargs):
    # 1. cls() call Python automatically new object create
    obj = cls.__new__(cls)        # new object create
    cls.__init__(obj, *args, **kwargs)  # constructor (__init__) call
    return obj

class Car:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing car of {self.width}x{self.height}")

rect = newFind(Car, 10, 20)
rect.draw()

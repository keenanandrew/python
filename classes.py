# how to create a class - a template for a type of object

class Point():
    # the below is the 'magic method', a function/method that's automatically
    # called every time I create a new point
    # self represents the object in question
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val


p = Point(2, 8)
print(p.x)
print(p.y)

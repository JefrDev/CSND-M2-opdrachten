# Replace the function definitions by the correct implementation.
class Rectangle:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def describe(self):
        return f'This %sx%s rectangle has an area of %s' % (self.x, self.y, self.area())


first = Rectangle(3, 5)
second = Rectangle(2, 1)
third = Rectangle(4, 3)

for r in [first, second, third]:
    print(r.describe())

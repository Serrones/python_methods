import math


class MyClass:
    def method(self):
        return 'instance method called', self
    
    @classmethod
    def class_method(cls):
        return 'class method called', cls

    @staticmethod
    def static_method():
        return 'static method called'

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius}, '
                f'{self.ingredients})')

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r**2 * math.pi
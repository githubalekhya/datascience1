class Fruit:
    name=""
    def __init__(self, color, flavor):
        self.flavor=flavor
        self.color=color
    def __str__(self):
        return "This fruit is {} of color {} and its flavor is {}".format(self.name, self.color, self.flavor)
class Apple(Fruit):
    pass
class Grape(Fruit):
    pass
apple=Apple("red", "sweet")
apple.name="apple"
grape=Grape("purple", "tart")
grape.name="grape"
print(apple)
print(grape)

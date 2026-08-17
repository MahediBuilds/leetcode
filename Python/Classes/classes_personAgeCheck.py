class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age > 17


p1 = Person("Zain", 21)
print(p1.is_adult())

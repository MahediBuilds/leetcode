class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, name):
        self.name = name
        print(self.name)


p1 = Person("Zain", 21)
p1.change_name("Ahmed")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name : " + self.name)
        print(f"Age : {self.age}")


p1 = Person("Zain", 21)
p1.display_info()

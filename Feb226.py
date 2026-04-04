# day 33
# classes and instant methods

class Dog:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Dog.count += 1

    def greet(self):
        print(
            f"hello {self.name}, you are currently a {self.species}")

    def rename(self, new_name):
        self.name = new_name

    @classmethod
    def reset(cls):
        cls.count = 0


s1 = Dog("Patrick", "Chihuahua.")
s2 = Dog("Alex", "Labrador Retriever")

s1.greet()
s2.greet()
print("The amount of dogs founded is:", Dog.get_count())
s1.rename("Ben")
s1.greet()
Dog.reset()
print(Dog.get_count())

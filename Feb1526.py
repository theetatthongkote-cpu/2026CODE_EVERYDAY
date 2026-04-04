# day 46
# __str__ method by myself
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # def __str__(self):
        # return f"Student(name='{self.name}', age={self.age}, grade='{self.grade}')"

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, grade='{self.grade}')"


Archi = Student("Archi", 20, "A")
Alex = Student("Alex", 21, "B")

Arc_info = repr(Archi)
Arc_object = eval(Arc_info)
print(type(Arc_object))
print(Arc_object.name)

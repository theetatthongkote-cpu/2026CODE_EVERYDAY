# day 32
# classes

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return (f"{self.name}{self.gpa}")

    @classmethod
    def get_count(cls):
        return f"Total number of students:{cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return (f"The average gpa of this glass is {cls.total_gpa / cls.count}")

    @classmethod
    def reset_class(cls):
        cls.count = 0
        cls.total_gpa = 0


student1 = Student("Patrick", 3.9)
student2 = Student("ALex", 3.7)
student3 = Student("Bob", 2.7)
student4 = Student("Spongebob", 3.0)

print(Student.get_count())
print(Student.get_average_gpa())

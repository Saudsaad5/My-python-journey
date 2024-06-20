class Student:

    class_year =2025
    num_stud = 0

    def __init__(self, name, age):

        self.name = name
        self.age = age
        Student.num_stud += 1

student1 = Student("Saud", 23)
student2 = Student("Eyad", 21)
student3 = Student("Saher", 22)
student4 = Student("Suhaib", 22)

print(f"My graduating class of {Student.class_year} has {Student.num_stud} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
        
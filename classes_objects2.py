from classes_objects import Student

Student1 = Student("Tim", "CS", 3.4)
Student2 = Student("Tom", "Art", 1.2)

print(Student1.classname)
print(Student2.classgpa)

print(Student1.on_honor_roll())
print(Student1.goodGPA())
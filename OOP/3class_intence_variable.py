class Student:
    school_name= "Sumalian high school"

    def __init__(self, name):
        self.student_name= name

student1= Student("Ali")
print(f"Student name: {student1.student_name}, School name: {student1.school_name}")
    
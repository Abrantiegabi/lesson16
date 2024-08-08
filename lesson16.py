class Course:
    def __init__(self, course_name, instructor):
        self.course_name = course_name
        self.instructor = instructor
        self.students = []

    def add_student(self, name, age, grade):
        student = [{"name" : name, "age" : age, "grade" : grade}]
        self.students.append(student)
        print(f'{name} added to the course successfully!')

    def update_student(self, name, age=None, grade=None):
        for student in self.students:
            if student["name"] == name:
                if age is not None:
                    student["age"] = age
                if grade is not None:
                    student["grade"] = grade
                print(f"{name}'s data updated successfully")
                return
        print(f'{name} not found')

    # def remove_student(self, name):
    #     for student in self.students:
    #         if student["name"] == name:
    #             self.students.remove(student)
    #             print(f"{'name'} was removed from course successfully!")
    #             return
    #     print(f'{"name"} was not found!')

    def get_student_info(self):
        if not self.students:
            print("No student has enrolled for this course.")
            return
        for student in self.students:
            print(f'Name: {student["name"]}, Age: {student["age"]}, Grade: {student["grade"]}')


course = Course("Python Backend", "Nat Maestro")

course.add_student('Gabriel', 20, "A")
course.add_student('Alice', 24, "A+")
course.add_student('Dave', 29, "B")

# course.remove_student('Dave')

print(f'Course Name: {course.course_name}')
print(f'Instructor: {course.instructor}')

course.get_student_info()
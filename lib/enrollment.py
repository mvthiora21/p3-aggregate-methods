from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        if num_courses == 0:
            return 0
        average_grade = total_grades / num_courses
        return average_grade

class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()

class Enrollment:
    all = []

    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count

# Example Usage

# Create some students and courses
student1 = Student('Alice')
student2 = Student('Bob')
course1 = Course('Math 101')
course2 = Course('History 202')

# Enroll students in courses
student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course1)

# Set grades for student1
student1._grades[student1.get_enrollments()[0]] = 85  # Math 101
student1._grades[student1.get_enrollments()[1]] = 90  # History 202

# Aggregate methods usage
print(f"{student1.name} is enrolled in {student1.course_count()} courses.")
# Output: Alice is enrolled in 2 courses.

print(f"{student1.name}'s average grade is {student1.aggregate_average_grade()}.")
# Output: Alice's average grade is 87.5.

print(f"Enrollments per day: {Enrollment.aggregate_enrollments_per_day()}.")
# Output example: Enrollments per day: {datetime.date(2023, 5, 2): 3}
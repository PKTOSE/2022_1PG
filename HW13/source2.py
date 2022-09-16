class Person:
    def __init__(self,name,number):
        self.name = name
        self.number = number

class Student(Person):
    UNDERGRADUATE = 0
    POSTGRADUATE = 1
    def __init__(self,name,number,studentType):
        super().__init__(name,number)
        self.studentType = studentType
        self.gpa = 0
        self.classes = []

    def enrollCourse(self,course):
        self.classes.append(course)

    def __str__(self):
        return '\n이름 = {}\n주민번호 = {}\n수강과목 = {}\n평점 = {}'.format(self.name,self.number,self.classes,self.gpa)

class Teacher(Person):
    def __init__(self,name,number):
        super().__init__(name,number)
        self.courses = []
        self.salary = 3000000

    def assignTeaching(self,course):
        self.courses.append(course)

    def __str__(self):
        return '\n이름 = {}\n주민번호 = {}\n강의과목 = {}\n월급 = {}'.format(self.name,self.number,self.courses,self.salary)

print('(1)----Person 클래스 상속에 의한 Student 및 Teacher 클래스 생성')
hong = Student('홍길동','1234567',Student.UNDERGRADUATE)
hong.enrollCourse('자료구조')
print(hong)

kim = Teacher('김철수','1234567890')
kim.assignTeaching('Python')
print(kim)
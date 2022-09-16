# 클래스 기반의 성적처리
def createStudent(name,korean,math,eng,sci):
    return {
        'name':name,
        'kr':korean,
        'math':math,
        'en':eng,
        'sci':sci
    }
def getSum(std):
    return std['kr']+std['math']+std['en']+std['sci']
def getAvg(std):
    return getSum(std)/4
def toString(std):
    return '{}  {}\t{}\t'.format(std['name'],getSum(std),getAvg(std))

students = [
    createStudent('윤인성',87,98,88,95),
    createStudent('연하진',92,98,96,98),
    createStudent('구지연',76,96,94,90),
    createStudent('나선주',98,92,96,92),
    createStudent('윤아린',95,98,98,98),
    createStudent('윤명월',64,88,92,92)
]
print('1)----------딕셔너리 기반')
print('이름','총점','평균',sep='\t')
for student in students:
    print(toString(student))

# class
class Student:
    def __init__(self,name,kr,math,eng,sci):
        self.name = name
        self.kr = kr
        self.math = math
        self.eng = eng
        self.sci = sci
    def getSum(self):
        return self.kr + self.math + self.eng + self.sci
    def getAvg(self):
        return self.getSum()/4
    def toString(self):
        return '{} {} {}'.format(self.name,self.getSum(),self.getAvg())

print('2)----------클래스 기반')
students = [
    Student('윤인성',87,98,88,95),
    Student('연하진',92,98,96,98),
    Student('구지연',76,96,94,90),
    Student('나선주',98,92,96,92),
    Student('윤아린',95,98,98,98),
    Student('윤명월',64,88,92,92)
]
print('이름  총점  평균')
for i in students:
    print(Student.toString(i))
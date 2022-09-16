김민수 = {
    'name' : '김민수',
    'assignment' : [80,50,40,20],
    'test' : [75, 75],
    'lab' : [78.20, 77.20]
}
이민아 = {
    'name' : '이민아',
    'assignment' : [82, 56, 44, 30],
    'test' : [83, 95],
    'lab' : [67.90, 78.72]
}
배철수 = {
    'name' : '배철수',
    'assignment' : [77,82,23,39],
    'test' : [78,77],
    'lab' : [80,80]
}
def getAvg(marks):
    totalSum = float(sum(marks));return totalSum/len(marks)

def calcTotalAvg(student):
    assignment = getAvg(student['assignment'])
    test = getAvg(student['test'])
    lab = getAvg(student['lab'])
    return (0.1*assignment + 0.7 *test + 0.2 *lab)

def assignLetterGrade(scr):
    if scr >= 90: return 'A'
    elif scr >= 80: return 'B'
    elif scr >= 70: return 'C'
    elif scr >= 60: return 'D'
    else: return 'F'

def classAvg(students:list):
    print('students 리스트를 출력합니다. - 딕셔너리들의 리스트에 주목')
    print(students,'\n')
    resultsList = []
    for student in students:
        stdAvg = calcTotalAvg(student)
        resultsList.append(stdAvg)
    return getAvg(resultsList)

students = [김민수, 이민아, 배철수]

for i in students:
    print(i['name'])
    print('==========')
    print('{}의 총점 = {:.2f}'.format(i['name'],calcTotalAvg(i)))
    print('{}의 Grade = {}'.format(i['name'],assignLetterGrade(calcTotalAvg(i))) + '\n')

class_av = classAvg(students)
print('반 전체의 평균점수 = {:.2f}'.format(class_av))
print('반 전체의 평균 Grade = {}'.format(assignLetterGrade(class_av)))


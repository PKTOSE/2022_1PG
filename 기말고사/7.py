김민수 = {'이름': '김민수', '숙제': [10, 9, 10, 8, 10], '시험': [65, 75], '출석': [29]}
이민아 = {'이름': '이민아', '숙제': [10, 9, 10, 10, 10], '시험': [75, 85], '출석': [29]}
배철수 = {'이름': '배철수', '숙제': [10, 9, 10, 9, 10], '시험': [80, 88], '출석': [30]}

weight = [25, 30, 40, 5] # 숙제 중간 기말 출석  반영률
students = [김민수, 이민아, 배철수]

students_grade = []
def calc_grade(std:dict):
    hw = std['숙제']
    test = std['시험']
    attendence = std['출석']

    total = sum(hw)/50 * weight[0] + test[0]/100 * weight[1] + test[1]/100 * weight[2] + attendence[0]/30 * weight[3]
    return total
results = 0 # 전체 평균용
for i in students:
    result = calc_grade(i)
    results += result
    if result >= 90:
        students_grade.append((i['이름'], 'A'))
    elif result >= 80:
        students_grade.append((i['이름'], 'B'))
    elif result >= 70:
        students_grade.append((i['이름'], 'C'))
    elif result >= 60:
        students_grade.append((i['이름'], 'D'))
    else:
        students_grade.append((i['이름'], 'F'))

for i in students_grade:
    print(f'{i[0]}의 성적: {i[1]}')
else:
    print(f'전체 평균 총점: {results/len(students) :.2f}')
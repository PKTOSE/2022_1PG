# 주민번호 분석하기
print('(1)----------')

IDNum = input('주민번호를 입력하세요(xxxxxx-xxxxxxx)형태 : ').split('-')
print('생년월일 정보 : {}'.format(IDNum[0]))
month = int(IDNum[0][2:4])
date = int(IDNum[0][4:6])
gender = int(IDNum[1][0])
if gender == 1 or gender == 2: year='19'+IDNum[0][0:2]
else: year = '20'+IDNum[0][0:2]
age = 2022 - int(year) + 1
print('''
당신은 {}년에 태어나셨군요
당신의 생일은 {}월 {}일 이시군요
당신은 올해 {}살이군요
'''.format(year,month,date,age))
if gender == 1 or gender == 3: print('당신은 남성이군요')
else: print('당신은 여성이군요')

# 두개 이상의 데이터를 구분하여 입력하기
a,b = input('먹고싶은 과일 2개를 중간에 공란을 주고 입력하세요: ').split()
print('과일1 : {}\n과일2 : {}'.format(a,b))
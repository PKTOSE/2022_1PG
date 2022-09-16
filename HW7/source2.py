#성적 출력하기
def grade(n):
    if n>= 90:
        return 'A'
    elif n>=80:
        return 'B'
    elif n>=70:
        return 'C'
    elif n>=60:
        return 'D'
    else:
        return 'F'
print('성적 grade 확인')
scr = int(input('성적을 입력하세요 : '))
print('Grade = %s\n====================='%grade(scr))

#BMI 계산
def checkBMI(h,w):
    bmi = (w/(h*0.01)**2)
    if bmi >= 40:
        return bmi,'고도비만'
    elif bmi >= 30:
        return bmi, '비만'
    elif bmi >= 25:
        return bmi, '경도비만'
    elif bmi >= 20:
        return bmi, '정상체중'
    else:
        return '저체중 '
print('=====BMI 계산하기=====')
height = int(input('키가 몇 cm 인가요? :'))
weight = int(input('몸무게가 몇 kg 인가요? :'))
print('키 {}cm, 몸무게 {}kg에 대한 BMI지수는 {:.2f}, {}입니다.'.format(height,weight,*checkBMI(height,weight)))
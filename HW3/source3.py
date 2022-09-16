'''
Quiz) 표준 체중을 구하는 프로그램을 작성하시오

*표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m)^2 X 22
여자 : 키(m)^2 X 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        *함수명 : std_weight
        *전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''
def std_weight(height:int,gender:int):
    height *= 0.01
    if gender == 3:
        return '남자의 표준 체중은 %.2fkg 입니다.'%(height**2 * 22)
    else:
        return '여자의 표준 체중은 %.2fkg 입니다.'%(height**2 * 21)
height,gender = map(int, input('키와 성별을 입력해주세요 (남자면 3, 여자면 4 / 예. 175 3) : ').split())
print('키 {0}cm '.format(height) + std_weight(height,gender) )
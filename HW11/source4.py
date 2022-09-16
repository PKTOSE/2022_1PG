#클래스 기반의 연락처 관리
class Friend:
    def __init__(self,name,phone,email,adress):
        self.name = name
        self.phone = phone
        self.email = email
        self.adress = adress

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    # edit info
    def setName(self,newName):
        self.name = newName
        print('수정 완료')

    def setEmail(self,newEmail):
        self.email = newEmail
        print('수정 완료')

    def setPhone(self,newPhone):
        self.phone = newPhone
        print('수정 완료')

    def setAdress(self,newAdress):
        self.adress = newAdress
        print('수정 완료')

    def edit(self):
        print('1. 이름 수정\n2. 번호 수정\n3.메일 수정\n4.주소 수정')
        try:
            choseNum = int(input('번호를 입력하세요: '))
            if choseNum not in range(1, 5): print('메뉴를 찾을 수 없습니다.');raise
            replace = input('수정할 내용을 입력 하세요: ')
            if choseNum == 1: self.setName(replace)
            elif choseNum == 2: self.setPhone(replace)
            elif choseNum == 3: self.setEmail(replace)
            elif choseNum == 4: self.setAdress(replace)

        except:
            print('잘못 입력 하셨습니다.')

    def showINFO(self):
        print('''
        이름:     {}
        전화 번호: {}
        e-mail:  {}
        주소:     {}'''.format(self.name,self.phone,self.email,self.adress))

frs = []
def main():
    while True:
        try:
            check = 0
            menu = int(input('\n1. 연락처 입력\n2. 연락처 출력\n3. 연락처 조회\n4. 연락처 수정\n5. 연락처 삭제\n6. 종료\n: '))
            if menu == 1: # 연락처 입력
                infos = list(input('이름, 번호, 메일, 주소: ').split())
                frs.append(Friend(*infos)) # 리스트를 unpack하여 Friend 객체를 만듦

            elif menu == 2: # 모든 연락처 출력
                for i in frs:
                    i.showINFO()

            elif menu == 3: # 연락처 조회
                print('어떤 연락처를 조회 하겠습니까?')
                for i in frs:
                    print(i.getName())
                name = input('이름을 입력하세요: ')
                for i in frs:
                    if name == i.getName():
                        i.showINFO()
                        check = 1
                else:
                    if not check:
                        print('이름을 찾지 못했습니다.')

            elif menu == 4: # 연락처 수정(모든 내용 수정 가능/한번에 한개씩만)
                print('어떤 연락처를 수정 하겠습니까?')
                for i in frs:
                    print(i.getName())
                name = input('이름을 입력하세요: ')
                for i in frs:
                    if name == i.getName():
                        i.edit()
                        check = 1
                else:
                    if not check:
                        print('이름을 찾지 못했습니다.')

            elif menu == 5: # 연락처 삭제
                print('어떤 연락처를 삭제 하겠습니까?')
                for i in frs:
                    print(i.getName())
                name = input('이름을 입력하세요: ')
                for i in frs:
                    if name == i.getName():
                        frs.remove(i)
                    check = 1
                else:
                    if not check:
                        print('이름을 찾지 못했습니다.')

            elif menu == 6: # 프로그램 종료
                print('프로그램을 종료합니다.')
                return

            if menu not in range(1,7): # 숫자 잘못 입력
                raise
        except: # 입력에 대한 모든 오류
            print('잘못입력하셨습니다.')
            continue

frs.append(Friend('윤지민','010-111-222','yjm@google.com','서울'))
frs.append(Friend('이선준','010-222-333','sjoon2@naver.com','서울'))
frs.append(Friend('장지우','010-333-444','pikachu@kakao.com','Tokyo'))
frs.append(Friend('윤지율','010-444-555','I_S2_@google.com','Seoul'))

main()

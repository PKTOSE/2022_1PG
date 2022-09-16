#클래스 기반의 연락처 관리
class Friend:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def setPhone(self,newPhone):
        self.phone = newPhone

    def showINFO(self):
        print('''
        이름    : {}
        전화번호 : {}'''.format(self.name,self.phone))

print('=-=-=(1)=-=-=')
f = Friend('윤성우','010-1234-1234')
f.setPhone('010-4321-4321')
f.showINFO()
print('=-=-=(2)=-=-=')
frs = []
frs.append(Friend('윤지민','010-111-222'))
frs.append(Friend('이선준','010-222-333'))
frs.append(Friend('장지우','010-333-444'))
frs.append(Friend('윤지율','010-444-555'))

for i in frs:
    i.showINFO()
print('=-=-=(3)=-=-=')
for i in frs:
    if i.getName().startswith('윤'):
        i.showINFO()
print('=-=-=(4)=-=-=')
for i in frs:
    if i.getName() == '장지우':
        i.setPhone('010-999-888')
for i in frs:
    if i.getName() == '장지우':
        i.showINFO()
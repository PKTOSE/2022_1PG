#연락처 관리 프로그램

def findFriend(friends:list,name:str): # 주소록에 이름이 있는지 확인
    if len(friends)==0: return True
    for i in range(len(friends)):
        if friends[i][0] == name:
            info = (i,friends[i])
            return info # 튜플 형태로 반환, 삭제 혹은 정보 변경을 위해 현재 인덱스 정보 저장 및 반환, 찾은 정보도 함께 반환
    return '이름을 찾을 수 없습니다.'

def printFriendList(friends:list): # 주소록 출력
    print(*('Name : {} | Phone Number : {}\n'.format(*a) for a in friends))

def addFriend(friends:list): # 주소록에 이름, 전화번호 튜플로 추가
    name = input('추가할 친구의 이름을 입력하세요: ')
    findFr = findFriend(friends,name)
    try:
        if findFr[1][0] == name: return print('이미 등록된 이름입니다.')
        else: raise
    except:
        phoneNum = input('친구의 전화번호를 입력하세요: ')
        plus = (name, phoneNum)
        friends.append(plus)

def delFriend(friends:list): # 이름 기반으로 주소록에 정보 삭제
    if len(friends) == 0:print('주소록이 비어있습니다.');return
    name = input('삭제할 친구의 이름을 입력하세요: ')
    findFr = findFriend(friends,name)
    if findFr[1][0] == name:
        friends.remove(friends[findFr[0]])
        print(f'{name}을(를) 삭제하였습니다.')
    else: print(findFr)

def rename(friends:list): # 이름 기반으로 주소록 이름 변경
    if len(friends) == 0: print('주소록이 비어있습니다.');return
    name = input('수정을 원하는 이름을 입력하세요: ')
    findFr = findFriend(friends,name)
    if findFr[1][0] == name:
        phone = findFr[1][1]
        friends.remove(friends[findFr[0]])
        changeName = input('변경할 이름을 입력하세요: ')
        friends.insert(findFr[0],(changeName,phone))
        print(f'{changeName}으로 변경 성공하였습니다.')
    else: print(findFr)

def main():
    friends = []
    while True:
        print('''
=====연락처 관리=====
1. 친구 리스트 출력
2. 친구 추가
3. 친구 삭제
4. 이름 변경
9. 종료
        ''')
        try:
            chose = int(input('메뉴를 선택하세요 : '))
        except:
            continue
        if chose == 1: printFriendList(friends)
        elif chose == 2: addFriend(friends)
        elif chose == 3: delFriend(friends)
        elif chose == 4: rename(friends)
        elif chose == 0: print(friends)
        else: return

main()
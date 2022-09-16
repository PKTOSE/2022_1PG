#연락처 관리 프로그램

def printFriendList(friends:list):
    print(*friends)

def addFriend(friends:list):
    name = input('추가할 친구의 이름을 입력하세요: ')
    friends.append(name)

def delFriend(friends:list):
    name = input('삭제할 친구의 이름을 입력하세요: ')
    try:
        friends.remove(name)
    except Exception as e:
        print('입력하신 이름이 잘못되었습니다.')


def rename(friends:list):
    name = input('수정을 원하는 이름을 입력해주세요: ')
    try:
        place = friends.index(name)
        friends.remove(name)
        changeName = input('변경할 이름을 입력하세요: ')
        friends.insert(place, changeName)
    except:
        print('이름을 찾을 수 없습니다.')

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
        chose = int(input('메뉴를 선택하세요 : '))
        if chose == 1: printFriendList(friends)
        elif chose == 2: addFriend(friends)
        elif chose == 3: delFriend(friends)
        elif chose == 4: rename(friends)
        else: return

main()
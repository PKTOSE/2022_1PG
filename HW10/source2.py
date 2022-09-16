dic = {}
fname = 'animal_eng.txt'
print('**파일 전체를 출력합니다.')

with open(fname, 'r', encoding='utf8') as file:
    print(file.read())

with open(fname, 'r', encoding='utf8') as file:
    for line in file.readlines():
        x = line.split(',')
        dic[x[0]] = x[1].replace('\n','').replace(' ','')
    print("**동물명 영어 사전을 출력합니다")
    print(dic)

while 1:
    query = input('\n동물 이름(한글): ')
    key = query.lower()
    if key in dic:
        eng = dic.get(key)
        print('{}는 영어로 {}입니다.'.format(query,eng))
    else:
        print('등록되지 않은 이름입니다.')
# idNum = ['030719-3123456','890312-2456754']
idNum = []
def anaylize():
    listOfTotal = {'b2000':0,'a2000':0,'ov40':0,'un40':0,'birth1-6':0,'birth7-12':0,'m':0,'f':0}
    for i in range(len(idNum)):
        month = int(idNum[i][2:4])
        gender = int(idNum[i][7])
        if gender == 1 or gender == 2: year = "19"+idNum[i][0:2]
        else: year = '20'+idNum[i][0:2]
        year = int(year)
        age=2022-year+1

        if year<2000:listOfTotal['b2000']+=1
        else:listOfTotal['a2000']+=1
        if age >= 40:listOfTotal['ov40']+=1
        else:listOfTotal['un40']+=1
        if month <= 6:listOfTotal['birth1-6']+=1
        else: listOfTotal['birth7-12']+=1
        if gender == 1 or gender == 3:listOfTotal['m']+=1
        else: listOfTotal['f']+=1
    return listOfTotal

with open('id.txt','r',encoding='utf8') as idFile:
    for i in idFile:
        idNum.append(i)

# for i in range(10):
#     id = idNum.append(input('주민번호를 입력해주세요 (xxxxxx-xxxxxxx) 형태: '))
result = anaylize()
print('''
2000년 이전에 태어난 사람 총 수 : {}
2000년 이후에 태어난 사람 총 수 : {}
나이가 40 이상인 사람 총 수     : {}
나이가 40 이하인 사람 총 수     : {}
태어난 월이 1-6월인 사람 총 수  : {}
태어난 월이 7-12월인 사람 총 수 : {}
남성 총 수                   : {}
여성 총 수                   : {}'''.format(result['b2000'],result['a2000'],result['ov40'],result['un40'],\
                                        result['birth1-6'],result['birth7-12'],result['m'],result['f']))
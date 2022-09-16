def tran(_list:list):
    toSTR = ''
    for i in _list:
        toSTR += i
        if i[-1] != '.':
            toSTR += ' '
    return toSTR

# li = ['This', 'is', 'the', 'final', 'exam.']
# print(tran(li))
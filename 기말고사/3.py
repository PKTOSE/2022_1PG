def reverseSTR(st:str):
    new_str = ''
    for i in range(len(st)-1, -1, -1):
        new_str += st[i]
    return new_str

# print(reverseSTR('abcde'))

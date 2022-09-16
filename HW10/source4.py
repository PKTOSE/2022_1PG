print('파일의 문자수, 단어 총 개수를 출력합니다)----------')
f = input('파일 이름을 입력해주세요 : ')
with open(f,'r',encoding='utf8') as file:
    strings = 0
    for i in file.readlines():
        i.split()
        for j in i:
            strings += 1
with open(f,'r',encoding='utf8') as file:
    words = 0
    text = file.read()
    text = text.split()
    words = len(text)
print('characters = {} (including spaces)\nwords = {}'.format(strings,words))

'''
사이트에서 특수문자가 많이 들어간 글은 단어인식이 제대로 안되는 문제를 확인했습니다.
글을 위의 코드와 MS워드에서의 단어수는 똑같은 값이 나왔지만, 사이트 상에선 더 많은 단어를
인식했다는 것을 확인했습니다.
'''
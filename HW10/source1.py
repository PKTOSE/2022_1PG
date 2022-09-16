print('1)----------')
f = input('파일 이름: ')
print('**파일 전체를 출력합니다.')
with open(f,'r') as file:
    print(file.read())

with open(f,'r') as file:
    table = dict()
    for i in file.readlines():
        words = i.split()
        for word in words:
            if word not in table:
                table[word] = 1
            else:
                table[word] += 1
    print('**단어별 빈도 수를 출력합니다.')
    print(table)

print('2)----------')
def parseFile(path):
    with open(path) as infile:
        spaces = 0
        tabs = 0
        for line in infile.readlines():
            spaces += line.count(' ')
            tabs += line.count('\t')
        return spaces,tabs
#f = input('파일 이름: ')
spaces, tabs = parseFile(f)
print('스페이스 수 = {}\n탭 수 = {}'.format(spaces,tabs))
# 회문인지 확인하기
def checkPal(word):
    low = 0; high = len(word)-1
    while True:
        if low > high: return True
        a=word[low];b=word[high]
        if a != b: return False
        low += 1; high -= 1

def getWord():
    s = input('input a string: ')
    print('회문입니까?')
    s = s.replace(' ','')
    return s

print('(1)----------------')
if checkPal(getWord()) == True: print('Yes')
else: print('No')

def checkPal1(word):
    for i in range(0,len(word)//2):
        if word[i] != word[len(word)-i-1]:return False
    return True

print('(2)----------------')
if checkPal1(getWord()) == True: print('Yes')
else: print('No')

def checkPal2(word):
    revWord = word[::-1]
    if word == revWord:return True
    return False

print('(3)----------------')
if checkPal2(getWord()) == True: print('Yes')
else: print('No')

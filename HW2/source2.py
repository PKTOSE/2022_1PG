'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) https://naver.com
규칙1 : https:// 부분은 제외 예-> naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
규칙3 : 남은 글자중 처음 세자리 + 글자 갯수 + 글자내 'e' 갯수 + '!'로 구성
            nav                 5              1            !
    => nav51!
'''
# 1. url 입력받아서 만들기
# 2. 'e'갯수 말고 'u'갯수로 만들기
# 3. 남은 글자중 뒤 3개

url = input('https://naver.com의 형태로 입력해주세요 : ')
url = url.replace('https://', '')
url = url.replace('http://', '')
url = url.replace('www.', '')
url = url[:url.index('.')]
passWord = url[-3:] + str(len(url)) + str(url.count('u')) + '!'
print(passWord)
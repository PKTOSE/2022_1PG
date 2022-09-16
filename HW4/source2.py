'''
Quiz) 당신의 회사에는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X주차 주간보고 -
부서 :
이름 :
업무요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt',... 와 같이 만듭니다.
'''
# 보고서에 이메일 항목 추가
# 몇주차 분량의 보고서를 만들것인지 입력받아서 처리 (최대 50주차까지만 입력하도록 함)
while 1:
    try:
        howMany = int(input("보고서를 몇주차까지 만들실 건가요? (최대 50주차) : "))
        if howMany > 50: raise Exception('숫자가 너무 커요..')
        break
    except Exception as e:
        print(e,'다시 입력해주세요')
        continue

for i in range(1,howMany+1):
    fileName = str(i)+'주차.txt'
    with open(fileName,'w',encoding='utf8') as weeklyReport:
        weeklyReport.write('''-{}주차 주간보고-
부서 : 
이름 : 
업무요약 : 
이메일 : 
        '''.format(i))
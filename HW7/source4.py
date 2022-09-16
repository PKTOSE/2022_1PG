# 성적 평균 및 grade 출력하기
def calcMean(scr: list): # 평균 계산
    totalScore = 0
    for i in scr:
        totalScore += i
    avgScr = totalScore/len(scr)
    return avgScr
def checkGrade(scr): # 등급 판별
    if scr>= 90:
        return 'A'
    elif scr>=80:
        return 'B'
    elif scr>=70:
        return 'C'
    elif scr>=60:
        return 'D'
    else:
        return 'F'
def main():
    scores = []
    print('학생들 성적의 평균점수와 grade를 출력합니다.')
    while True:
        scr = int(input('성적을 입력하세요 (더이상 입력할 값이 없으면 -1을 입력하세요) : '))
        if scr != -1:
            scores.append(scr)
        else: break
    avg = calcMean(scores)
    print("""
    =============================
    학생들 점수의 평균은 {:.2f}점 이며,
    평균점수에 대한 grade는 {}입니다.
    =============================
    """.format(avg,checkGrade(avg)))

main() # main 실행
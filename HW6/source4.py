# 성적 평균 구하기

def avgScore():
    print('학생들의 성적을 입력합니다. 평균을 계산합니다.\n입력을 종료하려면 -1을 입력하세요..')
    score=0
    numsOfStu = 0
    while True:
        scr = int(input('성적을 입력해주세요: '))
        if scr != -1:
            score += scr
            numsOfStu += 1
        else:
            return print('학생들 성적 평균은 {:.2f}점 입니다.'.format(score/numsOfStu))

avgScore()
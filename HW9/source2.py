# 문자열 내 특정 길이 이상의 단어 찾기

def findOverK(sentence,k:int):
    words = []
    sentence = [*sentence.split()]
    for i in range(len(sentence)):
        if len(sentence[i]) >= k:
            words.append(sentence[i])
    return words

sentence = input('input a sentence : ')
k = int(input('input a length k : '))
print(findOverK(sentence,k))
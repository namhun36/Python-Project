'''
영화 평점 1 ~ 5
평점을 입력받아서 범위 밖이면 다시 입력을 요구

이번 영화의 평점을 입력하세요 >>> 10
평점은 1~5사이만 입력할 수 있습니다
이번 영화의 평점을 입력하세요 >>> -2
평점은 1~5사이만 입력할 수 있습니다
'''

star = '*'

while True:
    score = int(input('이번 영화의 평점을 입력하세요 >>> '))
    if score >= 1 and score <= 5:
        print(f'평점 : {star * score}')
        break
    
    print('평점은 1~5사이만 입력할 수 있습니다')
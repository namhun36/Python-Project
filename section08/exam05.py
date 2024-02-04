'''
짝수인 구구단은 출력하지 말고(blank line)
홀수에 해당하는 단만 구구단을 출력하세요
구구단을 출력할때 곱수를 단수까지만 출력하세요
continue, break

3x1=3
3x2=6
3x3=9

5x1=5
5x2=10
5x3=15
5x4=20
5x5=25

7단은 7번
'''

# 4
for dan in range(2, 10):    # 단수
    if dan % 2 == 0:    # 짝수일때
       print()          # 공란 출력(Blank Line)
       continue

    for gop in range(1, 10):    # 곱수
        print(f'{dan} x {gop} = {dan*gop}')
        if gop == dan:
            break
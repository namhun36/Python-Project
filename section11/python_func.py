'''
파이썬의 특별한 함수 스타일
'''

# 코드의 생략
def pass_func():
    pass

# 가변 매개 변수
def show(*vals:int, horiz:int=1):
    print(vals)
    for n in vals:
        if horiz==1:
            print(n, end="\t")
        else:
            print(n)

    print()

def greet(message:str, temp: int, count:int=3):
    for n in range(count):
        print(message)

greet('안녕하세요', count=5)
greet('반갑습니다')

show(1,2,3,4,5, horiz=1)
show(1,2,3, horiz=0)
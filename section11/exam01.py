'''
700원짜리 윰료수 자판기
돈을 넣으면 몇잔의 음료수를 뽑을 수 있는지, 잔돈은 얼마인지
모든 경우의 수를 출력

함수정의
반환값 : 없음
함수 이름 : vaneindg_machin()
매게 변수 :  money (정수)

ending_machine(3000)
음료수 = 0개, 잔돈 = 3000원
'''

def vending_machine(money:int) -> None:
    value = 700
    count = 0
    while money > value:
        print(f'음료수 = {count}개, 잔돈 = {money}원')
        
        money -= value
        count += 1
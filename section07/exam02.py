'''
사용자로부터 양의 정수 입력받아
1 ~ 입력받은 정수까지의 합계를 출력

10
? = 1 + 2 + 3 + 4 + ... + 10
'''

total = 0
num = int(input('임의의 양의 정수를 입력하세요 >>> '))
for n in range(1, num+1):
    total += n

print(f'1부터 {num}사이 모든 정수의 합계는 {total}입니다.')
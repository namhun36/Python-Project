'''
내장 함수 : 파이썬 기본 패키지에 이미 포감되어서 제공하는 유틸리티(유용한?)

a = charg(12,3,4,5,6,) # 튜플

print('ㄹㄹㄹㄹㅇㅇㅇ')
val = input('프롬프트')
int('100')
float()
len(list)

메소드(Method) : 어떤 객체가 제공하는 기능
함수(Function) : 파이썬이 기본적으로 제공하는 기능

객체들
list, tupl,e set, dict, ''
'''

'{}이나 {}이면'.format(10, 20)

li = [1, 2, 3]
li.append(10)

print(chr(97))      # 해당 unicode의 문자를 반환한다
print(ord("한"))    # 문자를 unicode의 값으로 반환한다

val = eval('1*1') # 문자열로 수식을 입력하면 계산해서 그 값을 반환한다
print(val)












abs(-10)
round(10.5)


# 시퀀스에 관련됨 내장 함수들
# range()

li = [10, 20, 30, 40, 50]
for tp in enumerate(li):
    print(tp)


li = [5,3,4,2,8,1,9]
li2 = sorted(li)    # 오름차순 정렬
print( li2 )
li = sorted(li, reverse=False)  # 오름차순 정렬
print( li )




li = ['현대', '기아', '쌍용']
li2 = [1,2,3]

for comp in zip(li, li2):
    print(comp)
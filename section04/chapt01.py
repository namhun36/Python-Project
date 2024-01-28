'''
docstring 이란
docstring은 모듈, 함수, 클래스 또는 메소드 정의의 첫 번째 명령문으로 발생하는 문자열 리터럴
이러한 docstring은 해당 객체 의 doc 특수 속성으로 변환됨0
Docstring convention - https://www.python.org/dev/peps/pep-0257/

연산자와 우선순위
'''

'''
★ 산술연산자: +, -, *, /, //,%, **
    // -> 정수의 나누기, 몫만 취함
    %  -> 정수의 나누기, 나머지만 취함

★ 대입연산자: =, +=, -=, *=, /=, //=, %= **=

★ 관계연산자: >, >=, <, <=, ==
관계연산자의 결과는 True/False(논리값 -> boolean)로 정해진다
논리연산자: and, or, not
논리연산의 결과는 True/False(논리값 -> boolean)

비트연산자: &, |, ^, ~, <<, >>, >>>
1바이트는 8비트

기타연산자: 삼항연산자(참 if 논리식 else 거짓), in, +, *

'''

# print( 2 > 10 )
# result = 5 <= 10
# print( result )

# res1 = 5 == 10
# res2 = 5 <= 10
# print(res1, res2)

# False and True -> False (True and True 일 때만 True, 그 외 False)
# False Or True  -> True
# not True -> False

# result = res1 and res2
# print(result)

# result = res1 or res2
# print(result)

# result = not res2
# print(result)

age = int(input('나이를 입력하세요'))
# age가 10 보다 크고 18보다 작으면 청소년
result = (10 < age) and (age < 18)
if result:
    ls_text = '청소년 입니다'
else 
    ls_text = '청소년이 아닙니다'

print(ls_text)
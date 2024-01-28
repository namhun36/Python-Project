# 사람
# person = {}
# name: 
# age: 
# role: 
# {'name':'jhon', 'age':18, 'role':'아빠'}

# person = {}
# person = dict()
# person['name'] = input('이름을 입력 하세요')
# person['age']  = int(input('나이를 입력 하세요'))
# person['role'] = input('역할을 입력 하세요')
# print(person)

s_fm1_n = input('가족1_이름: ')
i_fm1_a = int(input('가족1_나이: '))
s_fm1_r = input('가족1_역할: ')

s_fm2_n = input('가족2_이름: ')
i_fm2_a = int(input('가족2_나이: '))
s_fm2_r = input('가족2_역할: ')

s_fm3_n = input('가족3_이름: ')
i_fm3_a = int(input('가족3_나이: '))
s_fm3_r = input('가족3_역할: ')


person1 = {}
person1 = dict()
person1.setdefault("p1_name", s_fm1_n)
person1.setdefault("p1_age",  i_fm1_a)
person1.setdefault("p1_role", s_fm1_r)

person2 = {}
person2 = dict()
person2.setdefault("p2_name", s_fm2_n)
person2.setdefault("p2_age",  i_fm2_a)
person2.setdefault("p2_role", s_fm2_r)

person3 = {}
person3 = dict()
person3.setdefault("p3_name", s_fm3_n)
person3.setdefault("p3_age",  i_fm3_a)
person3.setdefault("p3_role", s_fm3_r)

li = list()
li.append(person1)
li.append(person2)
li.append(person3)
print(li)


neighbor = dict()
# name: '댕댕이마을'
# family: list
# JSON 형식: 딕셔너리 하나 안에 리스트가 있고, 리스트 하위에 딕셔너리가 또 있다...(계층적 구조화 중요!)
# 요즘 파이썬으로 많이 개발 하는 것들. 매크로(자동화), AI, 빅데이터, 웹(백엔드)

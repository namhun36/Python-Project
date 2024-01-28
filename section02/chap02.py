'''
collection
list
tuple
set
dictionary
'''

# 빈리스트를 생성
# 추가/수정/삭제 O
li = []
li = [1,2,3,4,5]
print(li)
li.append(6)
li.append(7)
print(li)
li.remove(1)
print(li)

# 추가/수정/삭제 X
# 인덱싱 O
tp = tuple(li)

# 인덱싱 X
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(1)
print(s)

# 빈 딕셔너리를 만든다
# 인덱싱 O
# Key : Value의 쌍(couple)으로 데이터를 관리 한다.
di = dict()
di = {  #Key:Value
        "tomato":"토마토",
        "banana":"바나나",
        "apple":"사과"
    }
print(di)

# 싱글쿼터,더블쿼터 차이: 파이썬에서는 차이가 없음, 그러나 JSON에서는 더블쿼터를 사용 해야 함.
di['orange'] = '오렌지' #딕셔너리명[키값] = 밸류
di['apple']  = '애플'   #키값(왼쪽)이 같을 경우, 밸류를 업데이트
print(di)
print(di['tomato'])

some_fruit = '바나나의 키 값을 가져 와 some_fruit 변수에 삽입\n출력결과: ' + di['banana']
print(some_fruit)

# 딕셔너리와 유사하다. 파이썬 개발자들은 딕셔너리 보다 setdefault를 더 많이 사용 한다.
di.setdefault("tomato","토마토")
di.update(tomato="토마토")

# pop은 기존 딕션너리에서 값을 꺼내 주기(pop으로 사용한 데이터 기존 딕셔너리에서 삭제)
val = di.pop("tomato")
print(val)
print(di)


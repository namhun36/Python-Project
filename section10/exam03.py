'''
입력한 데이터를 각각 name과 store라는 변수에 저장하는 프로그램을 만드세요.

학생의 이름과 정수를 입력하세요 >>> 김철수,85

이름은 김철수이고, 점수는 85점입니다.
'''
# 김철수,85
student = input('학생의 이름과 정수를 입력하세요 >>> ')
li = student.split(',')
name = li[0]
store = name.split(',')[1]
print(li)
print(store)
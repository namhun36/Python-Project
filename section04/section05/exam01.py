# 1. 시험점수를 입력받아서...
# 100~90 : A
# 80~89 : B
# 70~79 : C
# 60~69 : D
# 그외에는 : F

# 점수를 입력하세요 >>> 90
# 점수는 90점이고, 학점은 A학점입니다.

score = int(input('점수를 입력하세요 >>> '))

if score <= 100 and score >= 90:
    grade = 'A'
elif score <= 89 and score >= 80:
    grade = 'B'
elif score <= 79 and score >= 70:
    grade = 'C'
elif score <= 69 and score >= 60:
    grade = 'E'
else:
    grade = 'F'

print(f'점수는 {score}점이고, 학점은 {grade}학점입니다.')
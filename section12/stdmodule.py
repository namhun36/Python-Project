'''
파이썬의 표준 모듈들...

'''
import math, random, time, datetime
import numpy as np
import requests

# 현재 시간
print(time.time())
print(time.ctime(time.time()))

# 시간 표시 형식 문자
# %Y : 년도수를 4자리로 표현
# %m : 월수를 1 ~ 12월로 표기
# %s : 일자를 1 ~ 31일로 표기
# %H : 시간을 24시간으로 표기
# %M : 분을 60분으로 표기
# %S : 초를 60초로 표기
# %a : 요일 영어로 표기
print( time.strftime('%Y-%m-%d %H:%M:%S %a') )


today = datetime.datetime.now()
today.year
today.month
today.date()

val = np.mean([10,20,30,40,50])

r = requests.get('https://www.naver.com')
print(r.text)
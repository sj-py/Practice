# 241
print("@ 241")
# import datetime module
import datetime
# get now time
now = datetime.datetime.now()
print(now,type(now))

# 242 243
print("@242, @243")
import datetime
now = datetime.datetime.now()

print('day')
for day in range(5,0,-1):
	# how to use timedelta method(days)
	delta = datetime.timedelta(days = day)
	date = now - delta
	print(date)
'''	
print('hour')
for hour in range(5,0,-1):
	# how to use timedelta method(hours)
	delta = datetime.timedelta(hours = hour)
	date = now - delta
	print(date)
	
print('minute')
for minute in range(5,0,-1):
	delta = datetime.timedelta(minutes = minute)
	date = now - delta
	print(date)
	
print('seconds')
for second in range(5,0,-1):
	delta = datetime.timedelta(seconds = second)
	date = now - delta
	print(date)
'''

# 244
print('@244')
import datetime
now = datetime.datetime.now()
print(now.strftime('%H:%M:%S'))

# 245
print('@245')
import datetime
day = "2023-05-18"
ret = datetime.datetime.strptime(day, '%Y-%m-%d')
print(day, type(day))
print(ret, type(ret))

# 246
print('@246')
import time
import datetime
i = 0
while i <= 2:
	print(datetime.datetime.now())
	i += 1
	time.sleep(1)
	
# 247
print('@247')
'''
1. import 모듈
- 모듈.함수 로 모듈내의 함수에 접근할 수 있다.
 
2. import 모듈 as 이름
- 모듈 내의 함수를 호출할 때 모듈 이름 대신 새 이름으로 함수를 호출하겠다는 뜻.
 
3. from 모듈 import 함수명
- 함수를 호출할 때 모듈 이름을 지정하지 않고, 바로 모듈 안의 함수를 호출할 수 있다.
 
4. from 모듈 import *
- 모듈 안에 있는 모든 것 (*)을 임포트하는 방식이다.
'''

# get an error on a phone
'''
# 248
print('@248')
import os
print(os.getcwd())

# 249
print('@249')
import os
os.rename("C:/Users/hyunh/Desktop/before.txt", "C:/Users/hyunh/Desktop/after.txt")
'''

# 250
print('@250')
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)

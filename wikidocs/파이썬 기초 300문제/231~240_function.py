# 231
print("@231")
def n_plus_1(n):
    result = n + 1
n_plus_1(3)
#print(result)
'''
#231번 문제는 print()함수안에 n_plus_1 함수의 지역변수인
result를 불러서 NameError이 발생한다
'''

# 232
print("@232")
def make_url(string):
    return "www." + string + ".com"
print(make_url("naver"))

# 233
print("@233")
def make_list(string):
    a = []
    for i in string :
        a.append(i)
    return a
print(make_list("abcd"))

# 234
print("@234")
def pickup_even(num):
    even = []
    for i in num:
        if i % 2 == 0: even.append(i)
    return even
print(pickup_even([2,3,4,5,6]))

# 235
print("@235")
def convet_int(string):
    return int(string.replace(",",""))
print(convet_int("1,234,567"))
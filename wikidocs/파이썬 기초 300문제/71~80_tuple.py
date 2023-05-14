'''
데이터 언패킹은 81번 문제
'''
# 71
my_variable = ()

# 72
movie_rank = ("닥터 스트레인즈", "스플릿", "럭키")

# 73
my_tuple = (1)
print(type(my_tuple))
my_tuple = (1,) # tuple에 데이터를 하나 저장시 ,를 반드시 붙여줘야함
print(type(my_tuple))

# 74
# tuple은 변경이 불가함 tuple is immutable

# 75
t = 1, 2, 3, 4
print(type(t))

# 76
t = ("a", "b", "c")
t = ("A", "b", "c") # 튜플의 요소를 바꾸려면 새로 선언해야함
print(t)

# 77
interest = ("삼성전자", "LG전자", "Sk Hynix")
interest = list(interest)
print(type(interest))

# 78 
interest = ["삼성전자", "LG전자", "Sk Hynix"]
interest = tuple(interest)
print(type(interest))

#79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 80
data = tuple((range(2,100,2)))
print(data)
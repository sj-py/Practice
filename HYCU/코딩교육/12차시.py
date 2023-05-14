# 해보기 1
# def getVal() :
#     a = int(input('val : '))
#     return a

# def add() :
#     a = getVal()
#     b = getVal()
#     return a + b

# def sub() :
#     a = getVal()
#     b = getVal()
#     return a - b

# def mul() :
#     a = getVal()
#     b = getVal()
#     return a * b

# def div() :
#     a = getVal()
#     b = getVal()
#     return a / b

# def ment() :
#     print("사칙연산을 수행합니다. 연산번호(1:add, 2:sub, 3:mul, 4:div, 5:end")
    
# while True :
#     ment()
#     choice = int(input("연산 번호 : "))
#     if choice == 1 :
#         print(add())
#     elif choice == 2 :
#         print(sub())
#     elif choice == 3 :
#         print(mul())
#     elif choice == 4 :
#         print(div())
#     elif choice == 5 :
#         print('end')
#     else : print("Wrong num, retry!")

# 해보기 2
# 해보기 1과 비슷함

# 해보기 3 로컬 변수 글로벌 변수
# num = 1 #g
# def test1(num) :#l
#     num = num + 1
#     print("num=",num)#l
# print("num=",num)#g
# test1(num)#g
# num = num + 1#g
# test1(num)#g

# 해보기 4
# def fibo(n) :
#     if n <= 2 :
#         return 1
#     else : return fibo(n - 2) + fibo(n - 1)
    
# def sum(n) :
#     i = 1
#     sum = 0
#     while i <= n :
#         print("fivo(",i,") =",fibo(i))
#         sum = sum + fibo(i)
#         i += 1
        
#     return sum
# n = int(input('n : '))
# print("fibo(1) ~",'fibo(',n,')까지의 합 =',sum(n))

# 해보기 5
# def tillSum(n) :
#     sum = 0
#     for i in range(1, n+1, 1) :
#         if i % 2 == 1 or i % 4 == 0 :
#             print(i)
#             sum += i
#     print("1 ~",n,"까지의 합 :", sum)
    
# n = int(input('n : '))
# tillSum(n)

# 해보기 6
# def getVal():
#     return (float(input('r : ')))

# def getArea():
#     a = getVal()
#     return a, a * a * 3.14

# print('r, area : ',getArea())

# 해보기 7
# def getVal() :
#     return (int(input()))

# def getArea2(a,b) :
#     print('가로 :', a, '세로 :', b, "넓이 :", a * b)

# print("가로, 세로의 길이를 차례대로 입력하세요(정수형태)")
# a = getVal()
# b = getVal()
# getArea2(a, b)

# 해보기 8
# pw = 'good'
# i = 1
# def getPw() :
#     global i
#     print("enter pw : ")
#     userPw = input()
#     if pw == userPw :
#         print(i,'번만에 맞춤')
#         return 1
#     i += 1

# while True :
#     if getPw() == 1 :
#         print("로그인 성공")
#         break

# 해보기 9

# 해보기 10
# import turtle as tt 
# t = tt.Turtle()
# a = ['pink', 'red', 'orange', 'purple']
# for i in a:
#     t.color(i)
#     t.forward(100)
#     t.right(90)

# 해보기 11
# import turtle
# import random as rd
# a = ['pink', 'red', 'orange', 'purple']
# b = rd.randint(1, 180)
# c = rd.randint(80, 90)
# j = 1
# tt = turtle.Turtle()
# while True :
#     if j == 11:
#         break
#     for i in a :
#         tt.color(i)
#         tt.forward(b)
#         tt.right(c)
#         b = rd.randint(1, 180)
#         c = rd.randint(80, 90)
#     j += 1

# 해보기 12
# st = []
# for i in range(5) :
#     print('name . st', i + 1, '=')
#     name = input()
#     st.append(name)
    
# sum = 0
# pre = 0
# for n in st:
#     print(n, 'score')
#     score = int(input())
#     sum = sum + score
#     pre += 1
    
# avg = sum // pre
# print('sum=', sum, 'avg=',avg)

# 해보기 13
# def CreList(n) : 
#     i = []
#     for j in range(n):
#         a = int(input('score : '))
#         i.append(a)
        
#     return i
# n = int(input('enter n : '))
# aList = CreList(n)
# print('aList = ', aList)


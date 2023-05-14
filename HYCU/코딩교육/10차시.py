# print("What a wonderful world")
# number = 1
# for i in range(5):
#     print("python good")

# print("단을 입력하세요(1~9)")
# dan = int(input())
# print("**************")
# for i in range(1,10,1):
#     print(dan,"*",i,"=",dan*i)
# print("**************")

# import random
# val = random.randint(1, 10)

# while True:
    
#     guess = int(input("1~10사이의 수를 예측해보세요 : "))

#     if val == guess:
#         print("Pass")
#         break # 반복문을 빠져나가는 명령어
#     elif val <= guess:
#         print("Down")
#     elif val >= guess:
#         print("Up")

# num = 1
# while True:
#     print("num:",num)
#     num += 1
#     if num % 7 ==0 :
#         break

# num = 1
# n = int(input("dan : "))
# for i in range(2,n+1,1):
#     print(n,"*",i,"=",n*i)

# n = int(input("몇단까지:"))
# n1 = int(input("출력하지 않을 단:"))
# num = 2
# for i in range(num, n+1, 1):
#     if i == n1:
#         continue
#     for j in range(1, 10):
#         print(i,"*",j,"=",j*i)

# while True:
#     dan = int(input("구구단을 출력할 단을 1~9사이의 숫자를 입력하시오 :"))
#     if dan < 1 | dan > 9:
#         print("다시입력")
#     else:
#         break
#     count = 1

# while True:
#     print(dan,"*",count,"=",dan*count)
#     count += 1
#     if count > 9:
#         break

# 1 ~ 100 까지의 수 중 2의 배수이거나 7의 배수인 경우의 합
# sum = 0 
# i = 0 
# n = int(input())
# while i <= n:
#     if i % 2 == 0 or i % 7 == 0:
#         sum = sum + i
#     i += 1

# print(sum)
# n = int(input("1~n까지 수중에서 2나 7의 배수의 합"))
# sum = 0
# for i in range(n+1):
#     if i % 2 == 0 or i % 7 == 0:
#         sum = sum + i
# print(sum)

# a ~ b까지 수중 2의 배수의 합 (3의배수는 제외)
# a = 0
# b = 0
# while a >= b:
#     a = int(input("a : "))
#     b = int(input("b : "))

# print("a :",a,"b :",b)

# sum = 0
# i = 0
# while i <= b:
#     i += 1
#     if i % 2 == 0:
#         if i % 3 == 0:
#             continue
#         else:
#             sum += i
# print(sum)

# 이진검색
# a = 1
# b = 30
# n = 0
# while n > 30 or n < 1:
#     n = int(input("n :"))

# print("n :",n)

# i = 1
# while a >= 1:
#     n2 = (a+b)//2
#     print(i,"번째 step","n2 :",n2)
#     if n2 == n:
#         print("성공",i,"번만에 찾음")
#         break
#     elif n > n2:
#         a = n2 + 1
#     elif n < n2:
#         b = n2 - 1
#     i += 1

# while True:
#     print("dan : ")
#     dan = int(input())
#     if dan < 1 or dan > 9:
#         print("retry")
#     if dan >= 1 and dan <= 9:
#         break
# count = 1
# while True:
#     print(dan,"*",count,"=",dan*count)
#     count += 1
#     if count > 9:
#         break

# while True:
#     print("dan : ")
#     dan = int(input())
#     if dan < 1 or dan > 9:
#         print("retry")
#     if dan >= 1 and dan <= 9:
#         break
# count = 1

# while True:
#     print(count,"단")
#     count2 = 1
#     while True:
#         print(count,"*",count2,"=",count*count2,end=" ")
#         count2 = count2 + 1
#         if count2 > 9:
#             break
#     count += 1
#     print()
#     if count > dan:
#         break

# sum = 0
# i = 0
# while True:
#     n = int(input('n :'))
#     if n > 1:
#         break

# while i <= n:
#     i += 1
#     if i % 3 == 0 and i % 5 == 0:
#         print(i,end=" ")
#         sum += i
# print(sum)

# import turtle as t
# t.shape('turtle')
# a=['red','orange','violet','lightsalmon','green','blue']
# for i in range(7):
#     t.color(a[i])
#     t.forward(100)
#     t.right(360/7)

#t.color("green","skyblue")
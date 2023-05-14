# 111
# n = input("문자열을 입력하시오 : ")
# print(n * 2)

# 112
# n = int(input("숫자를 입력하시오 : "))
# print(n + 10)

# 113
# n = int(input("숫자를 입력하시오 : "))
# if n % 2 == 0 :
#     print("짝수")
# else : 
#     print("홀수")

# 114
# n = int(input("입력값 : "))
# n += 20
# if n >= 255 :
#     n = 255
#     print("출력값 :", n)
# else : 
#     print("출력값 :", n)

# 115
# n = int(input("입력값 : "))
# n -= 20
# if n >= 255 :
#     n = 255
#     print("출력값 :", n)
# else : 
#     print("출력값 :", n)

# 116
# nowtime = input("현재시간 (형식 00:00) : ")
# if nowtime[3:] == "00":
#     print("정각 입니다.")
# else : 
#     print("정각이 아닙니다.")

# 117
# fruit = ["apple", "grape", "orange"]
# user = input("type a fruit : ")
# if user in fruit :
#     print("Correct!!!")
# else :
#     print("Wrong")

# 118
# warn_investment_list = ['Microsoft', 'Google', 'Naver', 'Kakao', 'SAMSUNG', 'LG']
# user = input("type a company you invest now : ")
# if user in warn_investment_list : 
#     print("WARNING!!")
# else : 
#     print("Safety")

# 119
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("type a fruit : ")
# if user in fruit.keys() :
#     print("Correct!!!")
# else :
#     print("Wrong")
    
# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("type a fruit : ")
if user in fruit.values() :
    print("Correct!!!")
else :
    print("Wrong")
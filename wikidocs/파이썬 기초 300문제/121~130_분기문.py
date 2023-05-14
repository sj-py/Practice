# 121
# user = input("type a letter : ")
# if user.islower( ) :
#     print(user.upper())
# else :
#     print(user.lower())

# 122
# score = int(input("score : "))
# if score > 80 :
#     print("A")
# elif score > 60 :
#     print("B")
# elif score > 40 :
#     print("C")
# elif score > 20 :
#     print("D")
# else :
#     print("E")

# 123
# user = input("how much do you have : ")
# user = user.split(" ")
# money = int(user[0])
# currency = user[1]
# if currency == "달러" :
#     print(money * 1167, "원")
# elif currency == "엔" :
#     print(money * 1.096, "원")
# elif currency == "유로" :
#     print(money * 1268, "원")
# elif currency == "위안" :
#     print(money * 171, "원")
# else :
#     print("It doesn't exist")
'''
user = input("how much do you have : ")
currency = {"달러" : 1167, "엔" : 1.096, "유로" : 1268, "위안" : 171}
money, a = user.split(" ")
print(int(money) * currency[a], "원")
'''

# 124
# num1 = int(input("num1 : "))
# num2 = int(input("num2 : "))
# num3 = int(input("num3 : "))
# print(max(num1, num2, num3))

# 125 value값을 이용해 key를 출력할 것임
'''
mobile_carrier = {"SKT" : "011", "KT" : "016", "LGU" : "019", "Unknown" : "010"}
user_phone_number = input("휴대폰 번호 : ")
for key, value in mobile_carrier.items() : # items 는 key : value를 쌍으로 tuple형식으로 얻을 수 있음
    if user_phone_number[:3] == value : 
        print(f"당신은 {key} 사용자입니다.")
'''

# 126
# address = int(input("우편번호 5자리를 입력하시오 : ")[2])
# if 0 <= address <= 2 :
#     print("강북구")
# elif 4 <= address <= 5 :
#     print("도봉구")
# else :
#     print("노원구")
    
# 127
# citizen_number = int(input("주민등록번호를 입력하시오 : ")[7])
# if citizen_number == 1 or citizen_number == 3 :
#     print("남자")
# else :
#     print("여자")

# 128
# citizen_number = int(input("주민등록번호를 입력하시오 : ")[8:10])
# if 0 <= citizen_number <= 8:
#     print("서울")
# elif 9 <= citizen_number <= 12 :
#     print("부산")
# else :
#     print("Unknown")

# 129 유효성 검사
# citizen_number = input("주민등록번호를 입력하시오 : ")
# num = 0
# for i in range(len(citizen_number)):
#     if citizen_number[i] == "-" :
#         continue
#     elif i == 0 or i == 9 :
#         num += int(citizen_number[i]) * 2
#     elif i == 1 or i == 10 :
#         num += int(citizen_number[i]) * 3
#     elif i == 2 or i == 11 :
#         num += int(citizen_number[i]) * 4
#     elif i == 3 or i == 12 :
#         num += int(citizen_number[i]) * 5
#     elif i == 4 :
#         num += int(citizen_number[i]) * 6
#     elif i == 5 :
#         num += int(citizen_number[i]) * 7
#     elif i == 7 :
#         num += int(citizen_number[i]) * 8
#     elif i == 8 :
#         num += int(citizen_number[i]) * 9
# num %= 11
# num = 11 - num
# if num == int(citizen_number[-1]):
#     print("pass")
# else :
#     print("wrong")

# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
move = int(btc["max_price"])-int(btc["min_price"]) + int(btc["closing_price"])
if move > int(btc["max_price"]) :
    print("상승장")
else : 
    print("하락장")
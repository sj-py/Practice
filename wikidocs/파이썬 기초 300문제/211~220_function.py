# 211
print("@211")
def 함수(문자열) :
    print(문자열)
함수("안녕")
함수("Hi")

# 212
print("@212")
def 함수(a, b) :
    print(a + b)
함수(3, 4)
함수(7, 8)

# 213
print("@213")
# def 함수(문자열) :
#     print(문자열)
# 함수()
'''함수안에 인자가 하나 주어지면 함수 부를 때 그 인자를 같이 넣어줘야 함'''

# 214
# print("@214")
# def 함수(a, b) :
#     print(a + b)
# 함수("안녕", 3)
'''함수를 부를 때 인자를 넣어준 것까지는 좋았지만 변수 타입이 다르다
변수 타입 또한 고려하여 맞춰 넣어줘야한다.'''

# 215
print("@215")
def print_with_smile(string) :
    print(string + ":D")
print_with_smile("Hi")

# 216
print("@216")
print_with_smile("안녕하세요")

# 217
print("@217")
def print_upper_price(price) :
    print("Upper price is " + str(price * 1.3))
print_upper_price(100)

# 218
print("@218")
def print_sum(a, b) :
    print(a, "+", b, "=", a+b)
print_sum(5, 5)

# 219
print("@219")
def print_arithmetic_operation(a, b) :
    print(a, "+", b, "=", a+b)
    print(a, "-", b, "=", a-b)
    print(a, "*", b, "=", a*b)
    print(a, "/", b, "=", a/b)
print_arithmetic_operation(3, 4)

# 220
print("@220")
def print_max(a, b, c) :
    result = 0
    if a > b and a > c : result = a
    elif b > a and b > c : result = b
    else : result = c
    print(result)
print_max(1, 2, 3)
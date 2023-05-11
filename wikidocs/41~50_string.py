# 41
ticker = "btc_krw"
print(ticker)
print(ticker.upper())

# 42
ticker = "BTC_KRW"
print(ticker)
print(ticker.lower())

# 43
string = 'hello'
print(string)
print(string.capitalize())

# 44
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx")) # Boolean

# 45
file_name = "보고서.xls"
print(file_name.endswith(("xlsx", "xls"))) # Boolean
'''
endswith() 메소드는 문자열이 주어진 접미사로 끝나면 True를 반환하고, 그렇지 않으면 False를 반환합니다. 
그러나 endswith() 메소드는 하나의 문자열 인수만 허용합니다.
따라서, endswith() 메소드에 인수를 하나만 전달해야 합니다. 
여러 개의 인수를 전달하려면, 다음과 같이 endswith() 메소드를 여러 번 호출하면 됩니다.
또는 endswith() 메소드에 하나의 문자열로 여러 개의 접미사를 전달하고, 이 문자열을 tuple 객체로 감싸면 됩니다.
하지만 이 경우에는 여러 개의 접미사 중 하나라도 일치하면 True를 반환합니다. 
따라서, xlsx와 xls를 구별하려면 위의 코드처럼 두 개의 endswith() 메소드 호출을 사용해야 합니다.
'''

# 46
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

# 47
a = "hello world"
print(a.split(" "))

# 48
ticker = "btc_krw"
ticker = ticker.split("_")
print(ticker)

# 49
date = "2020-05-01"
print(date.split("-"))

# 50
data = "039490       "
print(len(data))
data = data.rstrip()
print(len(data))
# 21
letters = 'python'
print(letters[0],letters[2])

# 22
license_plate = "24가 2210"
#print(license_plate[4:])
print(license_plate[-4:])

# 23
string = "홀짝홀짝홀짝"
print(string[::2])

# 24
string = "PYTHON"
print(string[::-1])

# 25
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

# 26
print(phone_number.replace("-", ""))

# 27
url = "http://sharebook.kr"
url_split = url.split(".")
print(url_split[1])

# 28
lang = "python"
#lang[0] = "P"
print(lang) # string is immutable(변경이 불가한)

# 29
string = 'abcdfe2a354a32a'
print(string.replace("a", "A"))
print(string) # the variable string is not changed

# 30
string = "abcd"
string.replace("b", "B")
print(string)
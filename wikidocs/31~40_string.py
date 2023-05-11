# 31
a = "3"
b = "4"
print(a + b) # these variables both are strings so it can't be added as math

# 32
print("Hi" * 3)

# 33
print("-" * 80)

#34
t1 = 'python'
t2 = 'java'
t3 = t1 + " " + t2 + " "
print(t3 * 4)

# 35
name1 = "kim minsu"
age1 = 10
name2 = "lee cheolhee"
age2 = 13
print("name:",name1,"age:",age1);print("name:",name2,"age:",age2)

# 36
print("name: {0} age: {1}".format(name1, age1))
print("name: {0} age: {1}".format(name2, age2))

# 37 f-string
print(f"name: {name1} age: {age1}")
print(f"name: {name2} age: {age2}")

# 38
상장주식수 = "5,969,782,550"
상장주식수 = int(상장주식수.replace(",", ""))
print(상장주식수, type(상장주식수))

# 39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 40
data = "   삼성전자    "
print(data)
print(data.strip())
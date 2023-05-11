# 내용 변경이나 추가는 불가하나 속도는 리스트보다 빠름
# 그래서 내용 변경이 없는 것들만 사용
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 오류가 남

name = "김종국"
age = 20
hobby = "coding"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "coding")
print(name, age, hobby)
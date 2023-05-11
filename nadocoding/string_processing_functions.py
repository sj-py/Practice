python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[0].islower())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n") # 첫 번째 위치를 알려줌
print(index)
index = python.index("n", index + 1) # 두 번째 위치를 알려줌
print(index)

print(python.find("n"))
print(python.find("Java")) # 값이 없을때 -1을 반환
#print(python.index("Java")) # 값이 없을때 오류가 발생함

print(python.count("n")) # 원하는 문자가 몇번 나오는지 알려줌
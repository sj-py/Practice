cabinet = {3 : "유재석", 100 : "김태호"} # key : value
print(cabinet[3]) # key 3의 값을 출력
print(cabinet[100])

print(cabinet.get(3)) # 위랑 같음
# print(cabinet[5]) # 없는 값은 오류가 남
print(cabinet.get(5)) # 값이 없어도 오류가 나지 않고 None이 나옴
print(cabinet.get(5, "사용가능")) # 값이 없을 때 원하는 내용 출력 가능
print('hi')

print(3 in cabinet) # 딕셔너리 안에 값이 있는지 확인
print(5 in cabinet)

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 값 업데이트
cabinet["C-20"] = "조세호" # 갑 추가
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values()) 

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)
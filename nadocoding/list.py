# list [] 순서가 있는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ['유재석', '조세호', '박명수']
print(subway)

# 조세호가 몇번째 칸에 타고 있는지
print(subway.index('조세호'))


# 다음 정류장에서 하하가 탔을때
subway.append('하하') # 맨 뒤에 붙음
print(subway)

# 정형돈이 유재석과 조세호 사이에 탔을때
subway.insert(1, "정형돈") # 원하는 위치에 원하는 값을 넣음
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop()) # 맨 뒤를 리스트에서 빼냄
print(subway)

# print(subway.pop()) # 맨 뒤를 리스트에서 빼냄
# print(subway)

# print(subway.pop()) # 맨 뒤를 리스트에서 빼냄
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [4,2,7,1,6]
num_list.sort() # 순서대로 정렬
print(num_list)

# 순서 뒤집기
num_list.reverse() 
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [4,2,7,1,6]
num_list.extend(mix_list)
print(num_list)
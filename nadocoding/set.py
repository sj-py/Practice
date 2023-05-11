# set 집합
# 중복이 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"Yu", "Kim", "Yang"}
python = set(['Yu', 'Park'])

# 교집합(java와 python을 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (java나 python을 할 수 있는 사람)
print(java | python)
print(java.union(python))

# 차집합(java는 할 수 있지만 python은 할 줄 모르는 사람)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("Kim")
print(python)

# java를 까먹었음
java.remove("Kim")
print(java)
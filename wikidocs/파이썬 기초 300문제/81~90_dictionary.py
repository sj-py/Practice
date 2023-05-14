# 81 별 표현식
'''기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 한다
하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있다
튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 
나머지 데이터의 언패킹 코드를 작성할 필요가 없다'''
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a)
print(b)
print(c) # star expression을 사용한 변수는 리스트 형식으로 저장

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)
print(len(valid_score))

# 82
a, b, *valid_score = scores
print(valid_score)

# 83
a, *valid_score, b = scores
print(valid_score)

# 84
temp = {}

# 85
ice = {"메로나" : 1000, "폴라포" : 1200, "빵빠레" : 1800}
print(ice)

# 86 딕셔너리에 값 추가
ice["죠스바"] = 1200
ice["월드콘"] = 1500
print(ice)

# 87
print("메로나 가격 :", ice["메로나"])

# 88 딕셔너리 value 값 수정
ice["메로나"] = 1300
print(ice)

# 89 딕셔너리 key 및 value 삭제
del ice["메로나"]
print(ice)

# 90
'''
딕셔너리 안에 업는 key를 호출시 에러가 발생함
'''
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("년생 : " + jumin[0:2]) # 0번째부터 2번째 직전 값까지(1번째까지)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 0은 명시할 필요없음
#print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 : " + jumin[7:]) # 끝까지 출력시 명시할 필요없음
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤 7번째부터 끝까지

# 61 리스트 슬라이싱
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 62 리스트 슬라이싱
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 63
print(nums[1::2])

# 64 리스트 뒤집기 by slicing
print(nums[::-1])

# 65
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 66 join 메소드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

# 67
print("/".join(interest))

# 68
print("\n".join(interest))

# 69 split 메소드
string = "삼성전자/LG전자/Naver"
print(string.split("/"))

# 70 리스트 정렬
data = [2, 4, 3, 1, 5, 10, 9]
print(data.sort()) # 출려값은 None
# 제대로 출력하는 방법
data.sort()
print(data)
print(sorted(data))
# 51
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

# 52 리스트에 요소 추가
movie_rank.append("베트맨")
print(movie_rank)

# 53 리스에 요소 삽입
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 54 리스트에서 요소 삭제
del movie_rank[3]
print(movie_rank)

# 55 리스트에서 요소 여러개 한번에 삭제
del movie_rank[2:]
print(movie_rank)

# 56 리스트 두개 합치기
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 57 리스트에서 최솟값과 최댓값 찾기
nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums)); print(min(nums))

# 58 리스트의 합
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 59 리스트에 저장된 데이터 갯수 구하기
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 60 리스트 평균 구하기
nums = [1, 2, 3, 4, 5]
print(sum(nums) / len(nums))
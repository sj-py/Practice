# 애완동물을 소개해주세요

name = "연탄이"
animal = "강아지"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "공놀이"

#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")

print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")

# +말고 ,를 사용하여 print에서 숫자 자료형이나 불리언을 출력할때에는 str이 필요없음

print(name + "는 어른일까요? " + str(is_adult))

# str(variable) = variable를 str형식으로 바꿔줌
# print는 str만 출력

'''주석의
또 다른 방법
편하게 하고 싶으면 ctrl + /를 누르면 일괄주석 
해제도 같음'''
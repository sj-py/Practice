# score = int(input("점수를 입력하시오 : "))
# if score >= 90:
#     print("grade = A")
# else :
#     if score >= 80 :
#         print("grade = B")
#     else :
#         if score >= 70 :
#             print("grade = C")
#         else :
#             if score >= 60 :
#                 print("grade = D")
#             else :
#                 print("다음 학기에 다시 수강 바랍니다.")

# if score >= 90 :
#     print("장학생",end=" ")
# else :
#     if score >= 60 :
#         print("합격",end=" ")
#     else :
#         print("불합격",end=" ")
# print("입니다")
for p in range(0, 3, 1):
    print("안녕하세요")
    
i, hap = 0, 0
for i in range(0, 11, 1):
    hap = hap + i
print("1엑서 10까지의 합계 : %d"%hap)

# i, gugudan = 0, 0
# gugudan = int(input("단을 입력하세요 : "))
# for i in range(1, 10, 1):
#     print("%d X %d = %2d"%(gugudan, i, gugudan * i))#2d는 정수를 2자리로 정의
    
for j in range(2, 10, 1):
    for k in range(1, 10, 1):
        print("%d X %d = %2d"%(j,k,j*k))
    print()
    
i, sum = 1, 0
while i < 21 :
    sum += i
    i += 1
print("1에서 20까지의 합 : %d"%sum)

sum = 0
for i in range(101):
    if i % 5 == 0 :
        continue
    sum += i
print(sum)

i, sum = 1, 0
while i < 101:
    if i % 5 == 0:
        i += 1
        continue
    sum += i
    i += 1
print(sum)

# 함수 선언
def add(m1, m2):
    result = 0
    result = m1 + m2
    return result
# 전역 변수 선언
hap = 0
# 메인 코드
hap = add(100,200)
print("100과 200의 add() 함수 결과는 %d"%hap)

# 함수 선언
def ssing1():
    a = 10 # 지역변수
    print("ssing1()에서 a값 %d"%a)
def ssing2():
    print("ssing2()에서 a값 %d"%a)
    
a = 20# 전역변수
ssing1()
ssing2()

ss = "파이썬"
print(ss.center(10))
print(ss.center(10, "-"))
print(ss.ljust(10))
print(ss.rjust(10))
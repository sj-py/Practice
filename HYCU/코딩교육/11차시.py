'''
def greeting():
    print("hi")
    print("good")
    print("bye")
    
greeting()

'''
'''
def add(n):
    return n, n + 100 # 두개 이상 리턴시 튜플형식으로 리턴됨
n = int(input("n : "))

re = add(n)
print(re)
'''

# 해보기 1번
'''
def add(a, b):
    print(a, "+", b, "=", a + b)

a = int(input("a : "))
b = int(input("b : "))

add(a, b)
'''

# 해보기 2번
'''
def add(a, b):
    return  a + b 

a = int(input("a : "))
b = int(input("b : "))

sum = add(a, b)
print(a, "+", b, "=", sum)
'''

# 해보기 3번
'''
import turtle
# 객체 생성 및 shape 설정등이 필요함 ####해보기 4번 참고####
def a():
    turtle.left(30)
    turtle.fd(100)
    
def b():
    turtle.right(30)
    turtle.fd(100)
    
turtle.onkeypress(a, "Up")
turtle.onkeypress(b, "Down")
'''

# 해보기 4번
'''
import random
import turtle

t = turtle.Turtle() # 객체 생성 방법
t.shape("turtle")

def left():
    t.left(30)
    t.forward(10)
    
def forwd():
    t.forward(10)
    
def backwd():
    t.backward(10)
    
def right():
    t.right(30)
    t.forward(10)
    
screen = t.getscreen()

screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(forwd, "Up")
screen.onkeypress(backwd, "Down")

screen.listen() # 코드 끝 부분에 위치하면 키 입력모드를 실행하도록 도와줌
'''
# 해보기 5번
'''
def stinfo(n):
    for i in range(n):
        학과 = input("학과 : ")
        학년 = input("학년 : ")
        grade = input("grade : ")
        print("학과 : ", 학과, "학년 : ", 학년, "grade : ", grade)
    
n = int(input("n : "))
stinfo(n)
'''
# 반지름
'''
def c_a(n):
    return n * n * 3.14

radius = float(input("radius : "))
print(c_a(radius))
'''

# 해보기 6번
'''
import turtle as tt
t = tt.Turtle()
t.shape("turtle")
t.color("orange", "yellow")

def opening():
    print("opening()을 통해 게임을 설명 \ndrawPol(n)을 호출하면 n각형의 도형을 그림\nleft(n)")
    
def drawPol(n):
    for i in range(n):
        t.fd(100)
        t.right(360/n)
        
def right(n):
    for i in range(n):
        t.fd(100)
        t.right(360/n)
        
def left(n):
    for i in range(n):
        t.fd(100)
        t.left(360/n)
        
drawPol(3)
'''

'''
a = 1
def test():
    global a
    a = 10
    b = 2
    return a + b
print(test())
print(a)
'''

'''
# 해보기 7번
def test():
    a = 3
    b = 2
    return a + b
print(test())
#print(a)
'''

'''
# 해보기 8번
def test():
    global a 
    a = 3
    b = 2
    return a + b
print(test())
print(a)
'''

'''
# 해보기 9번
a = 10
def test():
    global a
    a = 1
    b = 2
    return a + b
print(test())
print(a)
'''


# 연습문제 1
'''
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

a = int(input("a : "))
b = int(input("b : "))
'''
# 연습문제 2
'''
i = 1
while i <= 10:
    print("*")
    i += 1
'''
# 연습문제 3
'''
def t(n):
    for i in range(10):
        print(i)
'''        
# 연습문제 4
'''
for i in range(1, 10 ,2):
    print(i)
'''
# 연습문제 5
'''
def tillSum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    print(sum)
tillSum(9)    
'''
# 연습문제 7
'''
def getVal():
    a = float(input("radius : "))
    return a
    
def getArea(n):
    return n * n * 3.14
    
radius = getVal()
print(getArea(radius))
'''
# 연습문제 8
'''
def val():
    v=int(input("n:"))
    return v
def fac(n):
    fact=1
    for i in range(1,n+1):
        fact = fact * i
        
    return fact

a = val()
b = fac(a)
print(a, "의 팩토리얼", b)
'''
# 연습문제 9

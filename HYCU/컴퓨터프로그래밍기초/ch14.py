import turtle
import random
from tkinter.simpledialog import *

##전역 변수 선언 부분##
inputStr = ""
ttwidth, ttheight = 300, 300
turtleX, turtleY, turtleTsize = [0] * 3

##메인 코드 부분##
turtle.title("거북이로 글자쓰기")
turtle.shape("turtle")
turtle.setup(width = ttwidth + 50, height = ttheight + 50)
turtle.screensize(ttwidth, ttheight)
turtle.penup()

inputStr = askstring("입력받을 문자열 창", "거북이가 쓸 글자를 입력하세요")

for ch in inputStr:
    
    turtleX = random.randrange(-ttwidth/2, ttwidth/2)
    turtleY = random.randrange(-ttheight/2, ttheight/2)
    r = random.random(); g = random.random(); b = random.random()
    turtleTsize = random.randrange(25, 50)
    
    turtle.goto(turtleX, turtleY)
    
    turtle.pencolor((r,g,b))
    turtle.write(ch, font=('맑은고딕', turtleTsize, 'bold'))
    
turtle.done
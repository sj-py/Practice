# import turtle
# import random
# from tkinter.simpledialog import *

# ##전역 변수 선언 부분##
# inputStr = ""
# ttwidth, ttheight = 300, 300
# turtleX, turtleY, turtleTsize = [0] * 3

# ##메인 코드 부분##
# turtle.title("거북이로 글자쓰기")
# turtle.shape("turtle")
# turtle.setup(width = ttwidth + 50, height = ttheight + 50)
# turtle.screensize(ttwidth, ttheight)
# turtle.penup()

# inputStr = askstring("입력받을 문자열 창", "거북이가 쓸 글자를 입력하세요")

# for ch in inputStr:
    
#     turtleX = random.randrange(-ttwidth/2, ttwidth/2)
#     turtleY = random.randrange(-ttheight/2, ttheight/2)
#     r = random.random(); g = random.random(); b = random.random()
#     turtleTsize = random.randrange(25, 50)
    
#     turtle.goto(turtleX, turtleY)
    
#     turtle.pencolor((r,g,b))
#     turtle.write(ch, font=('맑은고딕', turtleTsize, 'bold'))
    
# turtle.done



## window
# from tkinter import *
# window = Tk()

# # button1 = Button(window, text="Quit IDLE", fg = 'green', bg = 'yellow', command=quit)
# # button1.pack()

# # radio button
# def radiFunc():
#     if var.get() == 1:
#         label1.configure(text = "python")
#     elif var.get() == 2:
#         label1.configure(text = "scratch")
#     else:
#         label1.configure(text = "java")
        
# var = IntVar()
# radi1 = Radiobutton(window, text='python', variable=var, value=1, command=radiFunc)
# radi2 = Radiobutton(window, text='scratch', variable=var, value=2, command=radiFunc)
# radi3 = Radiobutton(window, text='java', variable=var, value=3, command=radiFunc)

# label1 = Label(window, text='language', fg='black')

# radi1.pack()
# radi2.pack()
# radi3.pack()

# window.mainloop()

# photo album
from tkinter import *

photoName = ["!", "2", "#", "$", "%", "^", "&", "*", "()"]
num = 0

def goNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = photoName[num] # PhotoImage(file="경로" + photoName[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def goPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = photoName[num] # PhotoImage(file="경로" + photoName[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

window = Tk()
window.geometry("850x500")
window.title('travel')

Prev_btn = Button(window, text="<< Prev", command=goPrev)
Next_btn = Button(window, text="Next >>", command=goNext)

photo = photoName[num] # PhotoImage(file="경로" + photoName[num])
pLabel = Label(window, image = photo)

Prev_btn.place(x= 280, y = 470)
Next_btn.place(x=450,y= 470)

pLabel.place(x=15,y=10)

window.mainloop()
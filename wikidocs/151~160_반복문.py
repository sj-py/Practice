# 151
list = [3, -20, -3, 44]
for i in list :
    if i < 0 :
        print(i)
        
# 152
list = [3, 100, 23, 44]
for i in list :
    if i % 3 == 0 :
        print(i)
        
# 153
list = [13, 21, 12, 14, 30, 18]
for i in list :
    if i < 20 and i % 3 == 0 :
        print(i)
        
# 154
list = ["I", "study", "python", "language", "i"]
for i in list :
    if len(i) >= 3 :
        print(i)
        
# 155
list = ["A", "b", "c", "D"]
for i in list :
    if i.isupper() :
        print(i)
        
# 156
for i in list :
    if i.islower() :
        print(i)
        
# 157
list = ["dog", "cat", "parrot"]
for i in list:
    print(i.capitalize())
    
# 158
list = ['hello.py', "ex01.py", 'intro.hwp']
for i in list :
    print(i.split(".")[0])

# 159
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list :
    if i.split(".")[1] == "h": print(i)
    
# 160
for i in list :
    if i.split(".")[1] == 'h' or i.split(".")[1] == 'c' : print(i)
    
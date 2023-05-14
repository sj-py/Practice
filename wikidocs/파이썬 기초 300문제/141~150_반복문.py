# 141
list = [100, 200, 300]
for i in list:
    print(i + 10)
    
# 142
list = ["김밥", "라면", "튀김"]
for i in list :
    print("오늘의 메뉴 : " + i)
    
# 143
list = ["SK-Hynix", "Samsung", "LG"] 
for i in list :
    print(len(i))
    
# 144
list = ['dog', 'cat', 'parrot']
for i in list :
    print(i, len(i))
    
# 145
for i in list :
    print(i[0])
    
# 146, 147
list = [1, 2, 3]
for i in list :
    print("3 X", i, "=", 3 * i)
    
# 148
list = ["가", "나", "다", "라"]
for i in list[1:] :
    print(i)
    
# 149
for i in range(len(list)) :
    if i % 2 == 0 :
        print(list[i])
        
# 150
for i in list[::-1]:
    print(i)
# 181 2차원 리스트
apart = [['101호', '102호'],
         ['201호', '202호'],
         ['301호', '302호']]

# 182
stock = [['시가', 100, 200, 300],
         ['종가', 80, 210, 330]]

# 183
stock = {"시가" : [100, 200, 300], "종가" : [80, 210, 330]}

# 184 
stock = {"10/10" : [80, 110, 70, 90], "10/11" : [210, 230, 190, 200]}

# 185
apart = [['101호', '102호'],
         ['201호', '202호'],
         ['301호', '302호']]
for i in apart :
    for j in i :
        print(j)

print("-" * 10)   

# 186
for i in apart[::-1] :
    for j in i :
        print(j)
    
print('-' * 10)

# 187
for i in apart[::-1] : 
    for j in i[::-1] :
        print(j)
        
print("-" * 10)

# 188
for i in apart :
    for j in i :
        print(j)
        print("----")
        
print("-" * 10)

# 189
for i in apart :
    for j in i :
        print(j)
    print("-" * 4)
    
# 190
for i in apart :
    for j in i :
        print(j)
print("----")
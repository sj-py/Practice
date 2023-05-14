# 171
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)) :
    print(price_list[i])
    
# 172
for i in range(len(price_list)) :
    print(i, price_list[i])
    
# 173
for i in range(len(price_list)) :
    print((len(price_list) - 1) - i, price_list[i])
    
# 174
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])
    
# 175
my_list = ["가", "나", "다", "라"]
for i in range(3) :
    print(my_list[i], my_list[i + 1])
    
# 176
my_list.append("마") ; print(my_list)
for i in range(len(my_list) - 2) : print(my_list[i], my_list[i + 1], my_list[i + 2])

# 177
my_list.pop() ; print(my_list) # pop() = remove the last element in the list
for i in range(len(my_list) - 1, 0, -1) : print(my_list[i], my_list[i - 1])

# 178
my_list = [100, 200, 400, 800]
for i in range(len(my_list) - 1) : print(abs(my_list[i] - my_list[i + 1]))

# 179
my_list.extend([1000, 1300]) ; print(my_list)
for i in range(len(my_list) - 2) : print((my_list[i] + my_list[i + 1] + my_list[i + 2]) / 3)

# 180
low_price = [100, 200, 400, 800, 1000]
high_price = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_price)) : volatility.append(high_price[i] - low_price[i])
print(volatility)
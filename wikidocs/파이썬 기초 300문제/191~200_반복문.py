# 191 OHLC(open/high/low/close) fee = 0.014%
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for i in data :
    for j in i :
        print(j * 1.00014)
        
print("-" * 10)

# 192
for i in data :
    for j in i :
        print(j * 1.00014)
    print("----")
    
# 193
result = []
for i in data :
    for j in i :
        result.append(j * 1.00014)
print(result)

print("-" * 10)

# 194
result = []
for i in data :
    sub_list = []
    for j in i :
        sub_list.append(j * 1.00014)
    result.append(sub_list)
print(result)

print("-" * 10)

# 195 종가 출력
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc :
    if "close" in i :
        a = i.index("close")
    if type(i[0]) == int :
        print(i[a])
    
print("-" * 10)

# 196
for i in ohlc :
    if "close" in i :
        a = i.index("close")
    if type(i[0]) == int :
        if i[a] > 150 :
            print(i[a])
            
print("-" * 10)

# 197
for i in ohlc :
    if "open" in i : a = i.index("open")
    if "close" in i : b = i.index("close")
    if type(i[0]) == int and i[a] <= i[b] : print(i[b])
    
print("-" * 10)

# 198
volatility = []
for i in ohlc :
    if "high" in i : a = i.index("high")
    if "low" in i : b = i.index("low")
    if type(i[0]) == int :
        volatility.append(i[a] - i[b])
print(volatility)

print("-" * 10)

# 199
result = []
for i in ohlc : 
    if "open" in i : open = i.index("open")
    if "high" in i : high = i.index("high")
    if "low" in i : low = i.index("low")
    if "close" in i : close = i.index("close")
    if type(i[0]) == int and i[close] > i[open] : result.append(i[high] - i[low])
print(result)

print("-" * 10)

# 200
result = 0
for i in ohlc : 
    if "open" in i : open = i.index("open")
    if "close" in i : close = i.index("close")
    if type(i[0]) == int : result += (i[close] - i[open])
print(result)
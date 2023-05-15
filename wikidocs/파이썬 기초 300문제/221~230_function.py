# 221
print("@221")
def print_reverse(string) :
    print(string[::-1])
print_reverse("python")

# 222
print("@222")
def print_score(score_list) :
    print(sum(score_list)/len(score_list))
print_score([1,2,3])

# 223
print("@223")
def print_even(num_list) :
    even_list = []
    for i in num_list :
        if i % 2 == 0 : even_list.append(i)
    print(even_list)
print_even([1, 3, 2, 10, 12, 11, 15])

# 224
print("@224")
def print_keys(dict) :
    for i in dict.keys() :
        print(i)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225
print("@225")
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(my_dict, date) :
    print(my_dict[date])
print_value_by_key(my_dict, "10/26")

# 226
print("@226")
def print_5xn(string):
    num = int(len(string) / 5)
    for i in range(num + 1):
        print(string[i * 5 : i * 5 + 5])
print_5xn("아이엠어보이유알어걸")

# 227
print("@227")
def print_mxn(string, num):
    a = int(len(string) / num)
    for i in range(a + 1):
        print(string[i * num : i * num + num])
print_mxn("아이엠어보이유알어걸", 2) 

# 228
print("@228")
def calc_monthly_salary(annual_salary):
    print(int(annual_salary / 12))
calc_monthly_salary(12000000)

# 229
print("@229")
'''
왼쪽: 100
오른쪽: 200
'''

# 230
print("@230")
'''
229번과 반대
'''
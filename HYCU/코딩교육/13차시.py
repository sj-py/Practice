# n = int(input("input an integer : "))
# sum = 0
# for i in range(1, n + 1, 1):
#     sum += i
# print(sum)
# print(sum // n)

a = [1,2,3,4,5]
min = len(a) + 1
for i in a:
    if min > i:
        min = i
print(min)

max = -1
for i in a:
    if max < i:
        max = i
print(max)

#swap
a = 10
b = 20
print('a=',a,'b=',b)
temp = a
a = b
b = temp
print('a=',a,'b=',b)

arr = [5,9,1,3,4]
print("정렬 전")
for i in range(len(arr)):
    print(arr[i],end=",")
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print("정렬 후")
for i in range(len(arr)):
    print(arr[i],end=",")
    
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1, 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5,9,1,3,4]
print("정렬전")
for i in range(len(arr)):
    print(arr[i],end=",")
print()
print("정렬후")
bubbleSort(arr)
for i in range(len(arr)):
    print(arr[i],end=",")
print()
    
# fac
def fac(n):
    if n <= 1:
        return 1
    else:
        return n*fac(n-1)
print(fac(5))  
#fibo
def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)
print(fibo(10))
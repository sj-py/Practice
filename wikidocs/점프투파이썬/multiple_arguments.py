# how to get multiple arguments when you don't know how many arguments will input
def multiple_arguments(choice, *args):
	# sum
	if choice == 1:
		sum = 0
		for i in args:
			sum += i
		print(sum)
	# mul
	elif choice == 2:
		mul = 1
		for i in args:
			mul *= i
		print(mul)
multiple_arguments(2,1,2,3,4,5,6,7,8,9,10)

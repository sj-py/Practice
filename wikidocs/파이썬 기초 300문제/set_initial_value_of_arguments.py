# you can set the initial value of the arguments
# but if you set the value when you call the function
# the initial value will be replaced the value you use
def mul(a,b,c=10):
	print(a*b*c)

mul(1,2)
mul(1,2,3)

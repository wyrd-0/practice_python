def fib_gen(n):
	a,b,c = 1,0,0
	while n > 0:
		print("{}".format(a))
		n-=1
		c=b
		b=a
		a=b+c

while True:
	num = input("Give a number:  ")
	try:
		num = int(num)
	except ValueError:
		print("{} is not a number".format(num))
	if type(num) is int: break

fib_gen(num)

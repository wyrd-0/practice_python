while True:
	c = (input("Choose an option:\n(1) Check Divisibility\n(2)Check Evenness\n"))
	try:	
		c = int(c)
	except ValueError:
		print("Get that '{}' mess outta here!".format(c))
	if type(c) is int:
		if c==1 or c==2:
			break
		else:
			print("Get that '{}' mess outta here!".format(c))
if c == 1:
	m = input("Give the dividend:  ")
	n = input("And the divisor:  ")
	try:
		m = int(m)
	except ValueError:
		print("{} is not a number".format(m))
	try:
		n = int(n)
	except ValueError:
		print("{} is not a number".format(m))
	if (m % n) == 0:
		print("{} divides {}!".format(n,m))
	else:
		print("{} does not divide {}...".format(n,m))
else:
	n = int(input("Gimme a number! : "))
	if (n % 2) == 0:
		if (n % 4) == 0:
			print("{} is divisible by 4".format(n))
		else:
			print("{} is even.".format(n))
	else:
		print("{} is odd.".format(n))

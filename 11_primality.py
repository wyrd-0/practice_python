def check_prime(num):
	if num < 4:
		print ("1, 2, and 3 are trivially prime.")
		return
	for n in range(2, int(num/2) + 1):
		if (num%n) == 0: 
			print("{} is not prime.".format(num))
			break
		if n == int(num/2):
			print("{} is prime.".format(num))

while True:
	c = input("Give a number:\n")
	try:
		c = int(c)
	except ValueError:
		print("{} is not a number".format(c))
	if type(c) is int: break

check_prime(c)

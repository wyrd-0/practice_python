from random import randrange

while True:
	n = randrange(1,10)
	c = input("Try to guess a number 1-9 (or type 'exit' to end execution):\n")
	if c == 'exit': break
	try:
		c = int(c)
	except ValueError:
		print("{} is not a number".format(c))
	if type(c) is int:
		if c < 1 or c > 9: 
			print("{} is not in the range [1-9]".format(c))
			continue
		if c == n:
			print("You guessed right!!!")
		else: 
			print("You guessed wrong; the number was {}.".format(n))

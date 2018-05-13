while True:
	c = input("Give a number:\n")
	try:
		c = int(c)
	except ValueError:
		print("{} is not a number".format(c))
	if type(c) is int: break

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n = []

for e in a:
	if e < c: n.append(e)

print("{}".format(n))

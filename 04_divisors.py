while True:
	c = input("Give a number:\n")
	try:
		c = int(c)
	except ValueError:
		print("{} is not a number".format(c))
	if type(c) is int: break

a =[]
r = int(c/2) + 1

for n in range(1,r):
	if (c%n) == 0: a.append(n)

a.append(c)
print(a)

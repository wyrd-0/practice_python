from random import randint, randrange, sample

a_len, b_len = randint(10,15), randrange(10,15)

a = sample(range(1,100),a_len)
b = sample(range(1,100),b_len)

r = []

for e in a:
	if e in b and e not in r: r.append(e)

print("The intersection of\n{}\nand\n{}\nis:\n{}".format(a,b,r))

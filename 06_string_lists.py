s = input("Input a string:  ")
f = 0
l = len(s) -1


while f < l:
	if s[f] != s[l]:
		print("'{}' is not a palindrome...".format(s))
		break
	else:
		f += 1
		l -= 1

if f >= l: print("'{}' is a palindrome!".format(s))

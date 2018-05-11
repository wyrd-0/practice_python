from datetime import datetime

name = 	input("Hello, what's your name?  ")
age = 	int(input("How old are you, {}?  ".format(name)))
hunna = int(datetime.now().year) + 100  - age

print("You will turn 100 in the year {}, {}!".format(hunna, name))

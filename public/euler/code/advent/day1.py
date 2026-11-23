def readfile():
	with open("day1.txt") as fp:
		contents = fp.read()
		return contents

instructions = readfile()
floor = 0



for i,c in enumerate(instructions):
	if floor == -1:
		print(i)
		break
	if c == "(":
		floor += 1
	elif c == ")":
		floor -= 1

print(floor)
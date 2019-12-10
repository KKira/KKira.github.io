def readfile():
	with open("day3.txt") as fp:
		contents = fp.read()
		return contents

instructions = readfile()
x, y = 0, 0
x2, y2 = 0, 0
counter = {}
counter[(x,y)] = 1

for i, direction in enumerate(instructions):
	if i % 2 == 0:
		if direction == '<':
			x -= 1
		elif direction == '^':
			y += 1
		elif direction == '>':
			x += 1
		elif direction == 'v':
			y -= 1

		if (x,y) not in counter:
			counter[(x,y)] = 1
		else:
			counter[(x,y)] += 1

	else:
		if direction == '<':
			x2 -= 1
		elif direction == '^':
			y2 += 1
		elif direction == '>':
			x2 += 1
		elif direction == 'v':
			y2 -= 1

		if (x2,y2) not in counter:
			counter[(x2,y2)] = 1
		else:
			counter[(x2,y2)] += 1

print(len(counter))





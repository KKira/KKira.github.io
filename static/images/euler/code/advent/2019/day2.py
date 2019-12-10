def readfile():
	with open("day2.txt") as fp:
		contents = fp.read()
		positions = []
		for number in contents.split(','):
			positions.append(int(number))
		return positions

def read_instructions(instructions):
	for position in range(0, len(instructions), 4):
		if instructions[position]  == 1:
			instructions[instructions[position + 3]] = instructions[instructions[position + 1]] + instructions[instructions[position + 2]]
		elif instructions[position] == 2:
			instructions[instructions[position + 3]] = instructions[instructions[position + 1]] * instructions[instructions[position + 2]]
		elif instructions[position] == 99:
			return instructions[0]

instructions = readfile()

for x in range(0, 100):
	for y in range(0,100):
		instructions[1] = x
		instructions[2] = y
		if read_instructions(instructions) == 19690720:
			print(x, y)
			break
		else:
			instructions = readfile()
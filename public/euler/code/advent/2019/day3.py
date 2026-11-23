# def readfile():
# 	with open("day3.txt") as fp:
# 		contents = fp.read().strip()
# 		wires = []
# 		for wire in contents.split('\n'):
# 			wires.append([path for path in wire.split(',')])
# 		return wires

# wires = readfile()

# print(wires[0])
# print(wires[1])

tokens = {(1,1): '#', (5,6):'o'}
#function that prints grid x,y
def grid_generator(x,y):
	for width in range(x):
		for height in range(y):
			if width == 1 and height == 1:
				print('#', end='')
			elif width == 5 and height == 6:
				print('o', end='')
			else:
				print('.', end='')
		print('')

grid_generator(10,10)



# instructions = [['R',75],['D',30],['R',83],['U',83],['L',12],['D',49],['R',71],['U',7],['L',72],
# ['U',62],['R',66],['U',55],['R',34],['D',71],['R',55],['D',58],['R',83]]

# print(instructions)

# def grid_generator(instructions):
# 	for direction, steps in instructions:
# 		if direction == 'R':
# 			for step in range(steps):
# 				print('-', end='')
# 		elif direction == 'L':
# 			for step in range(steps):
# 				print('-', end='')
# 		elif direction == 'D':
# 			for step in range(steps):
# 				print('|', end='\n')
# 		elif direction == 'U':
# 			for step in range(steps):
# 				print('|', end='\n')

# print(grid_generator(instructions))




# print('.........')
# print('.........')
# print('.........')
# print('o', end="........")

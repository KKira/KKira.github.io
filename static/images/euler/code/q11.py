def readfile():
	with open("q11.txt") as fp:
		contents = fp.read()
		matrix = []
		for row in contents.split('\n'):
			matrix.append([int(n) for n in row.split(' ')])
		return matrix

def product(sequence):
	temp = 1
	for i in sequence:
		temp *= i
	return temp

def get_paths(x, y):
	return [[[x, y + n] for n in range(4)],
		   [[x + n, y] for n in range(4)], 
		   [[x + n, y + n] for n in range(4)],
		   [[x - n, y + n] for n in range(4)]]

matrix = readfile()
biggest = 0

for x in range(20):
	for y in range(20):
		for path in get_paths(x,y):
			try:
				sequence = [matrix[position[0]][position[1]] for position in path]
			except:
				continue

			temp = product(sequence)
			if biggest < temp:
				biggest = temp

print(biggest)





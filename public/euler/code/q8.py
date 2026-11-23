def readfile():
	with open("q8.txt") as fp:
		contents = fp.read()
		numbers = []
		for x in contents:
			if x == '\n':
				continue
			numbers.append(int(x))
		return numbers

def multiply_array(array):
	product = 1
	for x in array:
		product *= x
	return product

array_numbers = readfile()
biggest = 0

for i in range(len(array_numbers)):
	temp = multiply_array(array_numbers[i: i + 13])
	if temp > biggest:
		biggest = temp

print(biggest)
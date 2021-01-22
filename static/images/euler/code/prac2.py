def array_numbers():
	numbers = []

	for x in range(1, 5):
		numbers.append(x)

	return numbers

def multiply_array(array):
	product = 1
	for x in array:
		product *= x
	return product

print(array_numbers())
print(multiply_array(array_numbers()))
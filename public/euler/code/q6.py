def sum_of_squares():
	sum_natural = 0
	for n in range(101):
		n *= n
		sum_natural += n
	return sum_natural

def square_of_sums():
	square_sum = 0
	for n in range(101):
		square_sum += n
	square_sum *= square_sum
	return square_sum


print(sum_of_squares())
print(square_of_sums())
print(square_of_sums() - sum_of_squares())

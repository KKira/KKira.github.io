def fibonacci(term):
	numbers = [1,1]
	while numbers[-2] + numbers[-1] < term:
		numbers.append(numbers[-2] + numbers[-1])
	return numbers

def sum_even(numbers_array):
	even_numbers = []
	for x in numbers_array:
		if x % 2 == 0:
			even_numbers.append(x)
	return even_numbers



print(sum(sum_even(fibonacci(4000000))))

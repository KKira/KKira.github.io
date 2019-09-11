def calculate_fibo(max_term):
	new_term = 0
	prev1 = 1
	prev2 = 2
	sum_even = 0
	while (new_term<max_term):
		new_term = prev1 + prev2
		if(new_term % 2 == 0):
			sum_even += new_term
		# print(new_term)
		prev1 = prev2
		prev2 = new_term
	return sum_even


print(calculate_fibo(4000000))




